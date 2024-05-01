import os
import tkinter as tk

from path import Path


class ModelMenu:
    SEPALATER_NAMES = [
        "umiyuki-Japanese-Chat-Umievo-itr001-7b-Q4_K_M",
        "LightChatAssistant-4x7B-IQ4_XS",
        "JapaneseStarlingChatV-7B-Q4_K_M",
    ]

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="(New) モデル", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        for llm_name in self.ctx.llm:
            llm = self.ctx.llm[llm_name]
            llm_menu = tk.Menu(self.menu, tearoff=False)
            self.menu.add_cascade(label=llm_name, menu=llm_menu)

            if llm_name in self.SEPALATER_NAMES:
                self.menu.add_separator()

            llm_path = os.path.join(Path.kobold_cpp, llm["file_name"])
            if not os.path.exists(llm_path):
                llm_menu.add_command(
                    label="ダウンロード（完了まで応答なし、コマンドプロンプトに状況表示）",
                    command=lambda ln=llm_name: self.ctx.kobold_cpp.download_model(ln),
                )
                continue

            max_gpu_layer = llm["max_gpu_layer"]
            for gpu_layer in self.ctx["llm_gpu_layers"]:
                if gpu_layer > max_gpu_layer:
                    llm_menu.add_command(
                        label=f"L{max_gpu_layer}",
                        command=lambda ln=llm_name, gl=max_gpu_layer: self.select_model(ln, gl),
                    )
                    break
                else:
                    llm_menu.add_command(
                        label=f"L{gpu_layer}", command=lambda ln=llm_name, gl=gpu_layer: self.select_model(ln, gl)
                    )

    def select_model(self, llm_name, gpu_layer):
        self.ctx["llm_name"] = llm_name
        self.ctx["llm_gpu_layer"] = gpu_layer
        self.ctx.kobold_cpp.launch_server()
