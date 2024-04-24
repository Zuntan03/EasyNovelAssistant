import os
import tkinter as tk
import webbrowser


class HelpMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="ヘルプ", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)
        ena = "https://github.com/Zuntan03/EasyNovelAssistant"

        sample_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="サンプル原典", menu=sample_menu)

        cmd = lambda: self._show_url("https://kakuyomu.jp/works/16818093074043995181")
        sample_menu.add_command(label="最新AI Claude 3で長編小説執筆支援【GPT-4を超えた!?】", command=cmd)

        cmd = lambda: self._show_url("https://kakuyomu.jp/works/16818093074043995181/episodes/16818093074305285059")
        sample_menu.add_command(label="↑ のプロンプトまとめ", command=cmd)

        cmd = lambda: self._show_url("https://rentry.org/gpt0721")
        sample_menu.add_command(label="5ch プロンプトまとめ", command=cmd)

        reference_menu = tk.Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label="参照", menu=reference_menu)

        cmd = lambda: self._show_url("https://github.com/LostRuins/koboldcpp")
        reference_menu.add_command(label="LostRuins/KoboldCpp", command=cmd)

        self._show_hf_url(reference_menu, "Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF")
        self._show_hf_url(reference_menu, "Sdff-Ltba/LightChatAssistant-2x7B-GGUF")
        self._show_hf_url(reference_menu, "Aratako/LightChatAssistant-4x7B-GGUF")
        self._show_hf_url(reference_menu, "TFMC/Japanese-Starling-ChatV-7B-GGUF")
        self._show_hf_url(reference_menu, "andrewcanis/c4ai-command-r-v01-GGUF")
        self._show_hf_url(reference_menu, "dranger003/c4ai-command-r-plus-iMat.GGUF")
        self._show_hf_url(reference_menu, "pmysl/c4ai-command-r-plus-GGUF")

        self.menu.add_separator()
        cmd = lambda: self._show_url(ena)
        self.menu.add_command(label="EasyNovelAssistant", command=cmd)

    def _show_hf_url(self, menu, hf_name):
        cmd = lambda: self._show_url(f"https://huggingface.co/{hf_name}")
        menu.add_command(label=hf_name, command=cmd)

    def _show_url(self, url):
        webbrowser.open(url)
