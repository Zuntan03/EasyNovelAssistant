import os
import subprocess
import time
from sys import platform

import numpy as np
import requests
from job_queue import JobQueue
from path import Path
from scipy.io import wavfile


LEFT_DIALOGUE_QUOTE = "\u300c"
RIGHT_DIALOGUE_QUOTE = "\u300d"


class IrodoriTts:
    def __init__(self, ctx):
        self.ctx = ctx
        self.base_url = f'http://{ctx["irodori_tts_host"]}:{ctx["irodori_tts_port"]}'
        self.health_url = f"{self.base_url}/health"
        self.models_url = f"{self.base_url}/v1/models"
        self.voices_url = f"{self.base_url}/v1/audio/voices"
        self.speech_url = f"{self.base_url}/v1/audio/speech"

        self.models = None
        self.gen_queue = JobQueue()
        self.play_queue = JobQueue()

    def install(self):
        if platform == "win32":
            backend = "cu128" if self.ctx["irodori_tts_gpu"] else "cpu"
            self._run_bat(Path.irodori_tts_server_setup, "Irodori-TTS Server install", backend)
        else:
            msg = f"Install Irodori-TTS-Server into {Path.irodori_tts_server}, "
            print(msg + "then launch it with uv run python -m irodori_openai_tts.")

    def launch_server(self):
        if platform == "win32":
            host = self.ctx["irodori_tts_server_host"] or "0.0.0.0"
            cpu_arg = " --cpu" if not self.ctx["irodori_tts_gpu"] else ""
            command = f'{Path.irodori_tts_server_run} {host} {self.ctx["irodori_tts_port"]}{cpu_arg}'
            self._run_bat(command, "Irodori-TTS speech server")
        else:
            cpu_env = ""
            if not self.ctx["irodori_tts_gpu"]:
                cpu_env = "IRODORI_MODEL_DEVICE=cpu IRODORI_CODEC_DEVICE=cpu "
            host = self.ctx["irodori_tts_server_host"] or "0.0.0.0"
            command = (
                f'{cpu_env}uv run python -m irodori_openai_tts '
                f'--host {host} --port {self.ctx["irodori_tts_port"]}'
            )
            subprocess.Popen(command, cwd=Path.irodori_tts_server, shell=True)

    def is_installed(self):
        return os.path.exists(Path.irodori_tts_server)

    def is_installing(self):
        return self.is_installed() and (not os.path.exists(Path.irodori_tts_server_pyproject))

    def _run_bat(self, command, title, arg=""):
        if arg:
            command = f"{command} {arg}"
        subprocess.run(["start", title, "cmd", "/c", f"{command} || pause"], shell=True)

    def _headers(self, accept="application/json"):
        headers = {"accept": accept}
        api_key = self.ctx["irodori_tts_api_key"]
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        return headers

    def get_models(self):
        try:
            response = requests.get(
                self.voices_url,
                headers=self._headers(),
                timeout=self.ctx["irodori_tts_command_timeout"],
            )
            if response.status_code == 200:
                data = response.json()
                models = {}
                for voice in data.get("data", []):
                    voice_id = voice.get("id")
                    if voice_id:
                        models[voice_id] = {"id": voice_id}
                self.models = models
                return self.models
        except Exception:
            pass
        self.models = None
        return self.models

    def update(self):
        self.gen_queue.update()
        self.play_queue.update()

    def abort(self):
        self.gen_queue.cancel_all()
        self.play_queue.cancel_all()

    def generate(self, text, force=False):
        max_speech_queue = self.ctx["max_speech_queue"]

        if not force:
            if (self.gen_queue.len() > max_speech_queue) or (self.play_queue.len() > max_speech_queue):
                print(f"[Info] Speech queue is busy. Canceled Irodori-TTS speech: {text}")
                return False
        self.gen_queue.push(self._generate, text=text)
        return True

    def _generate(self, text):
        models = self.get_models()
        if models is None:
            return None

        voice_id, speech_text = self._select_voice_and_text(text, models)
        payload = self._build_payload(speech_text, voice_id)

        try:
            start_time = time.perf_counter()
            response = requests.post(
                self.speech_url,
                json=payload,
                headers=self._headers("audio/wav"),
            )
            if response.status_code == 200:
                os.makedirs(Path.daily_speech, exist_ok=True)
                YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                name = Path.get_path_name(speech_text[:128])
                wav_path = os.path.join(Path.daily_speech, f"{YYYYMMDD_HHMMSS}-irodori-{name}.wav")
                with open(wav_path, "wb") as f:
                    f.write(response.content)

                sample_rate, data = wavfile.read(wav_path)
                silence = np.zeros(int(sample_rate * self.ctx["speech_interval"]))
                data_with_silence = np.append(data, silence)
                wavfile.write(wav_path, sample_rate, data_with_silence.astype(np.int16))

                self.play_queue.push(self._play, wav_path=wav_path)
                print(f"Irodori-TTS speech {time.perf_counter() - start_time:.2f}s: {speech_text}")
                return True
            print(f"[Failed] IrodoriTts.generate(): {response.text}")
        except Exception as e:
            print(f"[Exception] IrodoriTts.generate(): {e}")
        return None

    def _select_voice_and_text(self, text, models):
        voice_id = self._fallback_voice(models, self.ctx["irodori_other_voice"])
        if LEFT_DIALOGUE_QUOTE in text:
            name, msg = text.split(LEFT_DIALOGUE_QUOTE, 1)
            if msg.endswith(RIGHT_DIALOGUE_QUOTE):
                msg = msg[:-1]
            if self.ctx["char_name"] in name:
                voice_id = self._fallback_voice(models, self.ctx["irodori_char_voice"])
                text = msg
            elif self.ctx["user_name"] in name:
                voice_id = self._fallback_voice(models, self.ctx["irodori_user_voice"])
                text = msg
        return voice_id, text

    def _fallback_voice(self, models, configured_voice):
        if configured_voice in models:
            return configured_voice
        if "none" in models:
            return "none"
        if len(models) > 0:
            return next(iter(models))
        return configured_voice or "none"

    def _build_payload(self, text, voice_id):
        payload = {
            "model": self.ctx["irodori_tts_model"] or "irodori-tts",
            "input": text,
            "voice": voice_id,
            "response_format": "wav",
            "irodori": {
                "chunking_enabled": bool(self.ctx["irodori_tts_chunking_enabled"]),
                "chunk_min_chars": int(self.ctx["irodori_tts_chunk_min_chars"]),
            },
        }

        first_sentence_min_chars = self.ctx["irodori_tts_first_sentence_chunk_min_chars"]
        if first_sentence_min_chars is not None:
            payload["irodori"]["first_sentence_chunk_min_chars"] = int(first_sentence_min_chars)

        num_steps = self.ctx["irodori_tts_num_steps"]
        if num_steps is not None:
            payload["irodori"]["num_steps"] = int(num_steps)

        return payload

    def _play(self, wav_path):
        subprocess.Popen(
            [
                "ffplay",
                "-volume",
                f'{self.ctx["speech_volume"]}',
                "-af",
                f'atempo={self.ctx["speech_speed"]}',
                "-autoexit",
                "-nodisp",
                "-loglevel",
                "fatal",
                wav_path,
            ],
            stdout=subprocess.DEVNULL,
        ).wait()
