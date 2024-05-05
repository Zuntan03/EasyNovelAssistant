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
        self.form.menu_bar.add_cascade(label="(New!) ツール", menu=self.menu)
        self.menu.configure(postcommand=self._on_menu_open)

    def _on_menu_open(self):
        self.menu.delete(0, tk.END)

        self.menu.add_command(label="(New!) 動画の作成", command=self.ctx.movie_maker.make)

        def set_subtitles(*args):
            self.ctx["mov_subtitles"] = self.subtitles_var.get()

        self.subtitles_var = tk.BooleanVar(value=self.ctx["mov_subtitles"])
        self.subtitles_var.trace_add("write", set_subtitles)
        self.menu.add_checkbutton(label="動画に字幕を追加", variable=self.subtitles_var)

        def set_resize(resize):
            self.ctx["mov_resize"] = resize

        self.resize_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'動画の長辺リサイズ: {self.ctx["mov_resize"]}px', menu=self.resize_menu)

        for resize in [1920, 1900, 1600, 1440, 1200, 1024, 0]:
            check_var = tk.BooleanVar(value=self.ctx["mov_resize"] == resize)
            cmd = lambda rs=resize, _=check_var: set_resize(rs)
            self.resize_menu.add_checkbutton(label=f"{resize}px", variable=check_var, command=cmd)

        def set_crf(crf):
            self.ctx["mov_crf"] = crf

        self.crf_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'動画の品質: CRF {self.ctx["mov_crf"]}', menu=self.crf_menu)

        for crf in [38, 32, 26, 20]:
            check_var = tk.BooleanVar(value=self.ctx["mov_crf"] == crf)
            cmd = lambda cr=crf, _=check_var: set_crf(cr)
            self.crf_menu.add_checkbutton(label=f"CRF {crf}", variable=check_var, command=cmd)

        def set_volume_adjust(*args):
            self.ctx["mov_volume_adjust"] = self.volume_adjust_var.get()

        self.volume_adjust_var = tk.BooleanVar(value=self.ctx["mov_volume_adjust"])
        self.volume_adjust_var.trace_add("write", set_volume_adjust)
        self.menu.add_checkbutton(label="動画の音量を 読み上げ音量 で調整", variable=self.volume_adjust_var)

        def set_tempo_adjust(*args):
            self.ctx["mov_tempo_adjust"] = self.tempo_adjust_var.get()

        self.tempo_adjust_var = tk.BooleanVar(value=self.ctx["mov_tempo_adjust"])
        self.tempo_adjust_var.trace_add("write", set_tempo_adjust)
        self.menu.add_checkbutton(label="動画の速度を 読み上げ速度 で調整", variable=self.tempo_adjust_var)

        self.menu.add_separator()

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
            url = "https://booth.pm/ja/search/Style-Bert-VITS2"
            self.menu.add_command(label="BOOTH (Style-Bert-VITS2)", command=lambda: webbrowser.open(url))
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
