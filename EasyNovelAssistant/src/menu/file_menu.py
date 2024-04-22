import os
import tkinter as tk
from tkinter import filedialog, messagebox

from path import Path


class FileMenu:
    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="ファイル", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

        self.form.win.bind("<Control-n>", lambda e: self.new_file())
        self.form.win.bind("<Control-o>", lambda e: self.open_file())
        self.form.win.bind("<Control-s>", lambda e: self.save_file())

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        self.menu.add_command(label="新規作成 (Ctrl+N)", command=self.new_file)

        self.menu.add_command(label="開く (Ctrl+O)", command=self.open_file)

        self.menu.add_separator()

        self.menu.add_command(label="保存 (Ctrl+S)", command=self.save_file)

        self.menu.add_command(label="名前を付けて保存", command=self.save_as_file)

        self.menu.add_separator()

        self.menu.add_command(label="終了 (Alt+F4)", command=self.ctx.finalize)

    def new_file(self):
        if not self.ask_save():
            return False
        self.ctx.input_area.set_text("")
        self.ctx.file_path = None
        self.ctx.file_text = ""
        self.form.update_title()
        return True

    def open_file(self):
        if not self.ask_save():
            return False
        if self.ctx.file_path is None:
            initial_dir = Path.cwd
        else:
            initial_dir = os.path.dirname(self.ctx.file_path)
        file_path = filedialog.askopenfilename(filetypes=[("テキストファイル", "*.txt")], initialdir=initial_dir)
        if file_path == "":
            return False
        return self._open_file(file_path)

    def dnd_file(self, event):
        file_path = event.data.strip()
        if file_path.startswith("{") and file_path.endswith("}"):
            file_path = file_path[1:-1]
        if not file_path.endswith(".txt"):
            return False
        if not os.path.exists(file_path):
            return False
        if not self.ask_save():
            return False
        return self._open_file(file_path)

    def _open_file(self, file_path):
        with open(file_path, "r", encoding="utf-8-sig") as f:
            input_text = f.read()
        self.ctx.input_area.set_text(input_text)
        self.ctx.file_path = file_path
        self.ctx.file_text = input_text
        self.form.update_title()
        return True

    def save_file(self):
        if self.ctx.file_path is None:
            return self.save_as_file()
        input_text = self.ctx.input_area.get_text()
        with open(self.ctx.file_path, "w", encoding="utf-8-sig") as f:
            f.write(input_text)
        self.ctx.file_text = input_text
        return True

    def save_as_file(self):
        if self.ctx.file_path is None:
            initial_dir = Path.cwd
        else:
            initial_dir = os.path.dirname(self.ctx.file_path)
        file_path = filedialog.asksaveasfilename(filetypes=[("テキストファイル", "*.txt")], initialdir=initial_dir)
        if file_path == "":
            return False
        if not file_path.endswith(".txt"):
            file_path += ".txt"

        input_text = self.ctx.input_area.get_text()
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write(input_text)
        self.ctx.file_path = file_path
        self.ctx.file_text = input_text
        self.form.update_title()
        return True

    def ask_save(self):
        input_text = self.ctx.input_area.get_text()
        if self.ctx.file_text == input_text:
            return True
        result = messagebox.askyesnocancel("EasyNovelAssistant", "変更内容を保存しますか？")
        if result is None:
            return False
        if result:
            return self.save_file()
        return True

    # TODO: watch_file
