import os
import tkinter as tk
import webbrowser

from path import Path


class SpeechMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="(New) 読み上げ", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        models = self.ctx.style_bert_vits2.models
        if models is None:
            models = self.ctx.style_bert_vits2.get_models()

        if models is None:
            if not os.path.exists(Path.style_bert_vits2):
                self.menu.add_command(
                    label="Style-Bert-VITS2 をインストール", command=self.ctx.style_bert_vits2.install
                )
            elif not os.path.exists(Path.style_bert_vits2_config):
                self.menu.add_command(label="Style-Bert-VITS2 のインストール中")
            else:
                self.menu.add_command(
                    label="読み上げサーバーを立ち上げる", command=self.ctx.style_bert_vits2.launch_server
                )

                def set_style_bert_vits2_gpu(*args):
                    self.ctx["style_bert_vits2_gpu"] = self.gpu_var.get()

                self.gpu_var = tk.BooleanVar(value=self.ctx["style_bert_vits2_gpu"])
                self.gpu_var.trace_add("write", set_style_bert_vits2_gpu)
                self.menu.add_checkbutton(label="GPU を使用する", variable=self.gpu_var)
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
        self.menu.add_cascade(label=f'読み上げ音量: {self.ctx["speech_volume"]}', menu=self.volume_menu)

        def set_speech_volume(volume):
            self.ctx["speech_volume"] = volume

        volumes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        for volume in volumes:
            check_var = tk.BooleanVar(value=self.ctx["speech_volume"] == volume)
            self.volume_menu.add_checkbutton(
                label=volume, variable=check_var, command=lambda v=volume, _=check_var: set_speech_volume(v)
            )

        self.speed_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'読み上げスピード: {self.ctx["speech_speed"]}', menu=self.speed_menu)

        def set_speech_speed(speed):
            self.ctx["speech_speed"] = speed

        speeds = [2.0, 1.75, 1.5, 1.25, 1.0, 0.75, 0.5]
        for speed in speeds:
            check_var = tk.BooleanVar(value=self.ctx["speech_speed"] == speed)
            self.speed_menu.add_checkbutton(
                label=speed, variable=check_var, command=lambda s=speed, _=check_var: set_speech_speed(s)
            )

        self.menu.add_separator()

        def set_char_voice(voice_name):
            self.ctx["char_voice"] = voice_name

        self.char_voice_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(
            label=f'{self.ctx["char_name"]} の声: {self.ctx["char_voice"]}', menu=self.char_voice_menu
        )

        for voice_name in models:
            check_var = tk.BooleanVar(value=self.ctx["char_voice"] == voice_name)
            self.char_voice_menu.add_checkbutton(
                label=voice_name, variable=check_var, command=lambda vn=voice_name, _=check_var: set_char_voice(vn)
            )

        def set_user_voice(voice_name):
            self.ctx["user_voice"] = voice_name

        self.user_voice_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(
            label=f'{self.ctx["user_name"]} の声: {self.ctx["user_voice"]}', menu=self.user_voice_menu
        )

        for voice_name in models:
            check_var = tk.BooleanVar(value=self.ctx["user_voice"] == voice_name)
            self.user_voice_menu.add_checkbutton(
                label=voice_name, variable=check_var, command=lambda vn=voice_name, _=check_var: set_user_voice(vn)
            )

        def set_other_voice(voice_name):
            self.ctx["other_voice"] = voice_name

        self.other_voice_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'その他の声: {self.ctx["other_voice"]}', menu=self.other_voice_menu)

        for voice_name in models:
            check_var = tk.BooleanVar(value=self.ctx["other_voice"] == voice_name)
            self.other_voice_menu.add_checkbutton(
                label=voice_name, variable=check_var, command=lambda vn=voice_name, _=check_var: set_other_voice(vn)
            )
