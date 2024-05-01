import json
import os
import subprocess
import time
from sys import platform

import numpy as np
import requests
from job_queue import JobQueue
from path import Path
from scipy.io import wavfile


class StyleBertVits2:
    SILENT_SEC = 0.3

    def __init__(self, ctx):
        self.ctx = ctx
        self.base_url = f'http://{ctx["style_bert_vits2_host"]}:{ctx["style_bert_vits2_port"]}'
        self.models_url = f"{self.base_url}/models/info"
        self.voice_url = f"{self.base_url}/voice"

        self.models = None
        self.gen_queue = JobQueue()
        self.play_queue = JobQueue()

    def install(self):
        if platform == "win32":
            self._run_bat(Path.style_bert_vits2_setup, "Style-Bert-VITS2 インストール")
        else:
            msg = f"{Path.style_bert_vits2} に Style-Bert-VITS2 をインストールして、"
            print(msg + "EasyNovelAssistant/setup/res/config.yml をインストール先にコピーしてください。")

    def launch_server(self):
        self._run_bat(Path.style_bert_vits2_run, "Style-Bert-VITS2 読み上げサーバー")

    def _run_bat(self, command, title):
        arg = "" if self.ctx["style_bert_vits2_gpu"] else " --cpu"
        if platform == "win32":
            subprocess.run(["start", title, "cmd", "/c", f"{command}{arg} || pause"], shell=True)
        else:
            python = os.path.join(Path.style_bert_vits2, "venv", "Scripts", "python")
            subprocess.Popen(f"{python} server_fastapi.py{arg}", cwd=Path.style_bert_vits2, shell=True)

    def get_models(self):
        try:
            response = requests.get(self.models_url, timeout=self.ctx["style_bert_vits2_command_timeout"])
            if response.status_code == 200:
                data = response.json()
                models = None
                for key in data:
                    model_id = int(key)
                    model_name = data[key]["id2spk"]["0"]
                    if models is None:
                        models = {}
                    models[model_name] = model_id
                self.models = models
                return self.models
        except Exception as e:
            pass
        self.models = None
        return self.models

    def update(self):
        self.gen_queue.update()
        self.play_queue.update()

    def generate(self, text):
        max_speech_queue = self.ctx["max_speech_queue"]
        if (self.gen_queue.len() > max_speech_queue) or (self.play_queue.len() > max_speech_queue):
            print(f"[Info] 混み合っているので読み上げをキャンセルしました。: {text}")
            return False
        self.gen_queue.push(self._generate, text=text)
        return True

    def _generate(self, text):
        models = self.get_models()
        if models is None:
            return None

        model_id = 0
        if "「" in text:
            name, msg = text.split("「", 1)
            if msg.endswith("」"):
                msg = msg[:-1]
            if self.ctx["char_name"] in name:
                if self.ctx["char_voice"] in self.models:
                    model_id = self.models[self.ctx["char_voice"]]
                    text = msg
            elif self.ctx["user_name"] in name:
                if self.ctx["user_voice"] in self.models:
                    model_id = self.models[self.ctx["user_voice"]]
                    text = msg
            else:
                if self.ctx["other_voice"] in self.models:
                    model_id = self.models[self.ctx["other_voice"]]

        params = {
            "text": text,
            "model_id": model_id,
            "split_interval": 0.2,
        }

        # model_id = 0
        # char_start = f'{self.ctx["char_name"]}「'
        # user_start = f'{self.ctx["user_name"]}「'
        # text = text.strip()
        # if text.startswith(char_start):
        #     if self.ctx["char_voice"] in self.models:
        #         model_id = self.models[self.ctx["char_voice"]]
        #     text = text[len(char_start) :]
        #     if text.endswith("」"):
        #         text = text[:-1]
        # elif text.startswith(user_start):
        #     if self.ctx["user_voice"] in self.models:
        #         model_id = self.models[self.ctx["user_voice"]]
        #     text = text[len(user_start) :]
        #     if text.endswith("」"):
        #         text = text[:-1]
        # else:
        #     if self.ctx["other_voice"] in self.models:
        #         model_id = self.models[self.ctx["other_voice"]]

        # nl_text = text
        # new_line_tokens = "。.！!？?…♪♥️♡"
        # for token in new_line_tokens:
        #     nl_text = nl_text.replace(token + token + token, token).replace(token + token, token)
        #     nl_text = nl_text.replace(token, f"{token}\n")
        # nl_text += "\n "

        # params = {
        #     "text": nl_text,
        #     "model_id": model_id,
        #     "split_interval": 0.2,
        # }

        try:
            start_time = time.perf_counter()
            response = requests.post(self.voice_url, params=params, headers={"accept": "audio/wav"})
            if response.status_code == 200:
                os.makedirs(Path.speech_date, exist_ok=True)
                YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                wav_path = os.path.join(Path.speech_date, f"{YYYYMMDD_HHMMSS}-{Path.get_path_name(text[:128])}.wav")
                with open(wav_path, "wb") as f:
                    f.write(response.content)

                # 無音の付与
                sample_rate, data = wavfile.read(wav_path)
                silence = np.zeros(int(sample_rate * self.SILENT_SEC))
                data_with_silence = np.append(data, silence)
                wavfile.write(wav_path, sample_rate, data_with_silence.astype(np.int16))

                self.play_queue.push(self._play, wav_path=wav_path)
                print(f"読み上げ {time.perf_counter() - start_time:.2f}秒: {text}")
                return True
            print(f"[失敗] StyleBertVits2.generate(): {response.text}")
        except Exception as e:
            print(f"[例外] StyleBertVits2.generate(): {e}")
        return None

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
            stdout=subprocess.DEVNULL,  # 終了時の改行対策、stderrは残す
        ).wait()
