import os
import subprocess
import tkinter as tk
import webbrowser
from sys import platform

from path import Path


class ToolMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="ツール", menu=self.menu)
        self.menu.configure(postcommand=self._on_menu_open)

    def _on_menu_open(self):
        self.menu.delete(0, tk.END)

        self.menu.add_command(label="KoboldCpp", command=self._run_kobold_cpp)

        if os.path.exists(Path.style_bert_vits2_config):
            self.menu.add_separator()
            self.menu.add_command(
                label="Style-Bert-VITS2 音声生成とモデル学習",
                command=lambda: self._run_style_bert_vits2(Path.style_bert_vits2_app, "app.py"),
            )
            self.menu.add_command(
                label="Style-Bert-VITS2 音声エディタ",
                command=lambda: self._run_style_bert_vits2(
                    Path.style_bert_vits2_editor, "server_editor.py --inbrowser"
                ),
            )

            self.menu.add_separator()
            url = "https://booth.pm/ja/items/5511852"
            self.menu.add_command(label="Anneli-nsfw 音声モデル", command=lambda: webbrowser.open(url))
            url = "https://booth.pm/ja/items/5511064"
            self.menu.add_command(label="Anneli 音声モデル", command=lambda: webbrowser.open(url))
            url = "https://booth.pm/ja/search/Style-Bert-VITS2"
            self.menu.add_command(label="BOOTH (Style-Bert-VITS2)", command=lambda: webbrowser.open(url))

            self.menu.add_separator()
            url = "https://booth.pm/ja/items/5511738"
            self.menu.add_command(label="黄琴まひろ (V3-JP-T)", command=lambda: webbrowser.open(url))
            url = "https://booth.pm/ja/items/5566669"
            self.menu.add_command(label="女子大生音声モデル", command=lambda: webbrowser.open(url))
            url = "https://huggingface.co/ayousanz/tsukuyomi-chan-style-bert-vits2-model"
            self.menu.add_command(label="つくよみちゃん 音声モデル", command=lambda: webbrowser.open(url))

    def _run_kobold_cpp(self, *args):
        if platform == "win32":
            command = ["start", "cmd", "/c"]
            command.append(f"{Path.kobold_cpp_win} || pause")
            subprocess.run(command, cwd=Path.kobold_cpp, shell=True)
        else:
            subprocess.Popen(f"{Path.kobold_cpp_linux}", cwd=Path.kobold_cpp, shell=True)

    def _run_style_bert_vits2(self, bat, py):
        if platform == "win32":
            subprocess.run(["start", "cmd", "/c", f"{bat} || pause"], cwd=Path.style_bert_vits2, shell=True)
        else:
            python = os.path.join(Path.style_bert_vits2, "venv", "Scripts", "python")
            subprocess.Popen(f"{python} {py}", cwd=Path.style_bert_vits2, shell=True)
