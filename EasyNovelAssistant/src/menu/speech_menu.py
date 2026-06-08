import tkinter as tk

from speech_manager import IRODORI_TTS, SPEECH_ENGINE_LABELS, normalize_speech_engine


class SpeechMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="読み上げ", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        def speech_all():
            text = self.ctx.form.input_area.get_comment_removed_text()
            lines = text.splitlines()
            for line in lines:
                self.ctx.speech.generate(line, force=True)

        self.menu.add_command(label="入力欄を読み上げ", command=speech_all)
        self.menu.add_command(label="読み上げを中断 (F5)", command=self.ctx.speech.abort)

        self.menu.add_separator()
        self._add_engine_menu()

        self.menu.add_separator()

        models = self.ctx.speech.models
        if models is None:
            models = self.ctx.speech.get_models()

        if models is None:
            engine_label = self.ctx.speech.active_label()
            if not self.ctx.speech.is_installed():
                self.menu.add_command(label=f"{engine_label} をインストール", command=self.ctx.speech.install)
            elif self.ctx.speech.is_installing():
                self.menu.add_command(label=f"{engine_label} のインストール中")
            else:
                self.menu.add_command(
                    label=f"{engine_label} 読み上げサーバーを立ち上げる",
                    command=self.ctx.speech.launch_server,
                )
            self._add_gpu_toggle()
            return

        def set_middle_click(*args):
            self.ctx["middle_click_speech"] = self.middle_click_var.get()

        self.middle_click_var = tk.BooleanVar(value=self.ctx["middle_click_speech"])
        self.middle_click_var.trace_add("write", set_middle_click)
        self.menu.add_checkbutton(label="中クリック読み上げ", variable=self.middle_click_var)

        def set_auto_speech_char(*args):
            self.ctx["auto_speech_char"] = self.auto_speech_char_var.get()

        self.auto_speech_char_var = tk.BooleanVar(value=self.ctx["auto_speech_char"])
        self.auto_speech_char_var.trace_add("write", set_auto_speech_char)
        self.menu.add_checkbutton(label=f'{self.ctx["char_name"]} 自動読み上げ', variable=self.auto_speech_char_var)

        def set_auto_speech_user(*args):
            self.ctx["auto_speech_user"] = self.auto_speech_user_var.get()

        self.auto_speech_user_var = tk.BooleanVar(value=self.ctx["auto_speech_user"])
        self.auto_speech_user_var.trace_add("write", set_auto_speech_user)
        self.menu.add_checkbutton(label=f'{self.ctx["user_name"]} 自動読み上げ', variable=self.auto_speech_user_var)

        def set_auto_speech_other(*args):
            self.ctx["auto_speech_other"] = self.auto_speech_other_var.get()

        self.auto_speech_other_var = tk.BooleanVar(value=self.ctx["auto_speech_other"])
        self.auto_speech_other_var.trace_add("write", set_auto_speech_other)
        self.menu.add_checkbutton(label="その他 自動読み上げ", variable=self.auto_speech_other_var)

        self.menu.add_separator()

        self.volume_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'読み上げ音量: {self.ctx["speech_volume"]}%', menu=self.volume_menu)

        def set_speech_volume(volume):
            self.ctx["speech_volume"] = volume

        volumes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        for volume in volumes:
            check_var = tk.BooleanVar(value=self.ctx["speech_volume"] == volume)
            self.volume_menu.add_checkbutton(
                label=f"{volume}%",
                variable=check_var,
                command=lambda v=volume, _=check_var: set_speech_volume(v),
            )

        self.speed_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'読み上げ速度: {self.ctx["speech_speed"]}倍', menu=self.speed_menu)

        def set_speech_speed(speed):
            self.ctx["speech_speed"] = speed

        speeds = [2.0, 1.75, 1.5, 1.25, 1.0, 0.75, 0.5]
        for speed in speeds:
            check_var = tk.BooleanVar(value=self.ctx["speech_speed"] == speed)
            self.speed_menu.add_checkbutton(
                label=f"{speed}倍",
                variable=check_var,
                command=lambda s=speed, _=check_var: set_speech_speed(s),
            )

        self.interval_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'読み上げ間隔: {self.ctx["speech_interval"]}秒', menu=self.interval_menu)

        def set_speech_interval(interval):
            self.ctx["speech_interval"] = interval

        intervals = [3.0, 2.0, 1.5, 1.0, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
        for interval in intervals:
            check_var = tk.BooleanVar(value=self.ctx["speech_interval"] == interval)
            self.interval_menu.add_checkbutton(
                label=f"{interval}秒",
                variable=check_var,
                command=lambda i=interval, _=check_var: set_speech_interval(i),
            )

        self.menu.add_separator()

        char_voice_key, user_voice_key, other_voice_key = self.ctx.speech.voice_keys()
        self._add_voice_menu(f'{self.ctx["char_name"]} の声', char_voice_key, models)
        self._add_voice_menu(f'{self.ctx["user_name"]} の声', user_voice_key, models)
        self._add_voice_menu("その他の声", other_voice_key, models)

    def _add_engine_menu(self):
        current_engine = normalize_speech_engine(self.ctx["speech_engine"])
        self.ctx["speech_engine"] = current_engine

        def set_speech_engine(*args):
            self.ctx["speech_engine"] = self.engine_var.get()

        self.engine_var = tk.StringVar(value=current_engine)
        self.engine_var.trace_add("write", set_speech_engine)
        self.engine_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(
            label=f"読み上げエンジン: {SPEECH_ENGINE_LABELS[current_engine]}",
            menu=self.engine_menu,
        )

        for engine, engine_label in SPEECH_ENGINE_LABELS.items():
            self.engine_menu.add_radiobutton(label=engine_label, variable=self.engine_var, value=engine)

    def _add_gpu_toggle(self):
        engine = self.ctx.speech.active_engine()
        if engine == IRODORI_TTS:
            key = "irodori_tts_gpu"
            label = "Irodori-TTS で GPU を使用する"
        else:
            key = "style_bert_vits2_gpu"
            label = "Style-Bert-VITS2 で GPU を使用する"

        def set_gpu(*args):
            self.ctx[key] = self.gpu_var.get()

        self.gpu_var = tk.BooleanVar(value=self.ctx[key])
        self.gpu_var.trace_add("write", set_gpu)
        self.menu.add_checkbutton(label=label, variable=self.gpu_var)

    def _add_voice_menu(self, label, key, models):
        def set_voice(voice_name):
            self.ctx[key] = voice_name

        voice_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f"{label}: {self.ctx[key]}", menu=voice_menu)

        for voice_name in models:
            check_var = tk.BooleanVar(value=self.ctx[key] == voice_name)
            voice_menu.add_checkbutton(
                label=voice_name,
                variable=check_var,
                command=lambda vn=voice_name, _=check_var: set_voice(vn),
            )
