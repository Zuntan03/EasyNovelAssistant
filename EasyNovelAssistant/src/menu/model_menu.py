import os
import tkinter as tk
from tkinter import simpledialog

from path import Path


class ModelMenu:
    SEPALATER_NAMES = [
        "LightChatAssistant-4x7B-IQ4_XS",
    ]

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="モデル", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        def context_label(context_size):
            return f"C{context_size // 1024}K ({context_size})"

        self.llm_context_size_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(
            label=f'コンテキストサイズ上限（増やすと VRAM 消費増）: {context_label(self.ctx["llm_context_size"])})',
            menu=self.llm_context_size_menu,
        )

        def set_llm_context_size(llm_context_size):
            self.ctx["llm_context_size"] = llm_context_size

        llm_context_sizes = [2048, 4096, 8192, 16384, 32768, 65536, 131072]
        for llm_context_size in llm_context_sizes:
            check_var = tk.BooleanVar(value=self.ctx["llm_context_size"] == llm_context_size)
            self.llm_context_size_menu.add_checkbutton(
                label=context_label(llm_context_size),
                variable=check_var,
                command=lambda v=llm_context_size, _=check_var: set_llm_context_size(v),
            )

        self.menu.add_separator()

        categories = {}

        for llm_name in self.ctx.llm:
            llm = self.ctx.llm[llm_name]

            llm_menu = tk.Menu(self.menu, tearoff=False)
            name = llm_name
            context_size = min(llm["context_size"], self.ctx["llm_context_size"]) // 1024
            if "/" in llm_name:
                category, name = llm_name.split("/")
                if category not in categories:
                    categories[category] = tk.Menu(self.menu, tearoff=False)
                    self.menu.add_cascade(label=category, menu=categories[category])
                categories[category].add_cascade(label=f"{name} C{context_size}K", menu=llm_menu)
            else:
                self.menu.add_cascade(label=f"{llm_name} C{context_size}K", menu=llm_menu)

            for sep_name in self.SEPALATER_NAMES:
                if sep_name in name:
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
        result = self.ctx.kobold_cpp.launch_server()
        if result is not None:
            print(result)
            simpledialog.messagebox.showerror("エラー", result, parent=self.form.win)
