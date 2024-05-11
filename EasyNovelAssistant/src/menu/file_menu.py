import glob
import os
import re
import shutil
import time
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
        self.form.win.bind("<Control-O>", lambda e: self.open_dir())
        self.form.win.bind("<Control-s>", lambda e: self.save_file())
        self.form.win.bind("<Control-S>", lambda e: self.save_all_file())
        self.form.win.bind("<Control-F4>", lambda e: self.close_file())

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        if len(self.ctx["recent_files"]) > 0:  # 最近使ったファイル、のカスケードメニューadd_cascade
            recent_files = tk.Menu(self.menu, tearoff=False)
            self.menu.add_cascade(label="最近使ったファイル", menu=recent_files)
            for file_path in reversed(self.ctx["recent_files"]):
                if os.path.exists(file_path):
                    recent_files.add_command(label=file_path, command=lambda fp=file_path: self._open_file(fp))
                else:
                    self.ctx["recent_files"].remove(file_path)

        if len(self.ctx["recent_dirs"]) > 0:  # 最近使ったフォルダ、のカスケードメニューadd_cascade
            recent_dirs = tk.Menu(self.menu, tearoff=False)
            self.menu.add_cascade(label="最近開いたフォルダ", menu=recent_dirs)
            for dir_path in reversed(self.ctx["recent_dirs"]):
                if os.path.exists(dir_path):
                    recent_dirs.add_command(label=dir_path, command=lambda dp=dir_path: self._open_dir(dp))
                else:
                    self.ctx["recent_dirs"].remove(dir_path)

        if (len(self.ctx["recent_files"]) > 0) or (len(self.ctx["recent_dirs"]) > 0):
            self.menu.add_separator()

        self.menu.add_command(label="新規作成 (Ctrl+N)", command=self.new_file)
        self.menu.add_command(label="開く (Ctrl+O)", command=self.open_file)
        self.menu.add_command(label="フォルダを開く (Ctrl+Shift+O)", command=self.open_dir)

        self.menu.add_separator()

        def _set_watch_file(*args):
            self.ctx["watch_file"] = self.watch_file_var.get()

        self.watch_file_var = tk.BooleanVar(value=self.ctx["watch_file"])
        self.watch_file_var.trace_add("write", _set_watch_file)
        self.menu.add_checkbutton(label="ファイル監視", variable=self.watch_file_var)

        self.menu.add_separator()

        self.menu.add_command(label="保存 (Ctrl+S)", command=self.save_file)
        self.menu.add_command(label="名前を付けて保存", command=self.save_as_file)
        self.menu.add_command(label="すべて保存 (Ctrl+Shift+S)", command=self.save_all_file)

        self.menu.add_separator()

        self.menu.add_command(label="閉じる (Ctrl+F4)", command=self.close_file)
        self.menu.add_command(label="すべて閉じる", command=self.close_all_file)

        self.menu.add_separator()

        self.menu.add_command(label="終了 (Alt+F4)", command=self.ctx.finalize)

    def new_file(self):
        input_area = self.ctx.form.input_area
        input_area.close_unmodified_new_tab()
        input_area.open_tab()
        self.form.update_title()

    def open_file(self):
        initial_path = self.ctx.form.input_area.get_file_path()
        if initial_path is None:
            initial_dir = Path.cwd
        else:
            initial_dir = os.path.dirname(initial_path)
        file_paths = filedialog.askopenfilename(
            filetypes=[("テキストファイル", "*.txt")], initialdir=initial_dir, multiple=True
        )
        if file_paths != "":
            for file_path in file_paths:
                self._open_file(file_path)

    def open_dir(self):
        initial_path = self.ctx.form.input_area.get_file_path()
        if initial_path is None:
            initial_dir = Path.cwd
        else:
            initial_dir = os.path.dirname(initial_path)
        dir_path = filedialog.askdirectory(initialdir=initial_dir)
        if dir_path != "":
            self._open_dir(dir_path)

    def dnd_file(self, event):
        file_paths = re.findall(r"\{[^}]*\}|[^ ]+", event.data)
        file_paths = [file_path.strip("{}") for file_path in file_paths]
        file_paths.sort()
        for file_path in file_paths:
            if file_path.endswith(".txt"):
                if os.path.exists(file_path):
                    self._open_file(file_path)
            elif os.path.isdir(file_path):
                self._open_dir(file_path)
        return "break"

    def _open_dir(self, dir_path):
        txt_files = glob.glob(os.path.join(dir_path, "**", "*.txt"), recursive=True)
        txt_files.sort()

        for file_path in txt_files:
            if os.path.exists(file_path):
                self._open_file(file_path)

        if dir_path in self.ctx["recent_dirs"]:
            self.ctx["recent_dirs"].remove(dir_path)
        self.ctx["recent_dirs"].append(dir_path)
        remove_num = len(self.ctx["recent_dirs"]) - self.ctx["recents"]
        if remove_num > 0:
            self.ctx["recent_dirs"] = self.ctx["recent_dirs"][remove_num:]

    def _open_file(self, file_path, func=None):
        input_area = self.ctx.form.input_area
        for tab in input_area.tabs:
            if tab.file_path == file_path:
                input_area.select_tab(tab)
                if not self.ask_save(func):
                    return

        input_area = self.ctx.form.input_area
        with open(file_path, "r", encoding="utf-8-sig") as f:
            input_text = f.read()
        input_area.close_unmodified_new_tab()
        input_area.open_tab(input_text, file_path)
        self.form.update_title()
        self._add_recent_file(file_path)

    def _add_recent_file(self, file_path):
        if file_path in self.ctx["recent_files"]:
            self.ctx["recent_files"].remove(file_path)
        self.ctx["recent_files"].append(file_path)
        remove_num = len(self.ctx["recent_files"]) - self.ctx["recents"]
        if remove_num > 0:
            self.ctx["recent_files"] = self.ctx["recent_files"][remove_num:]

    def save_file(self):
        input_area = self.ctx.form.input_area
        file_path = input_area.get_file_path()
        if file_path is None:
            return self.save_as_file()
        self._backup_file(file_path)
        input_text = input_area.get_text()
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write(input_text)
        input_area.set_file(input_text, file_path)
        self._add_recent_file(file_path)
        return True

    def save_as_file(self):
        input_area = self.ctx.form.input_area
        file_name = f'{time.strftime("%Y%m%d_%H%M%S", time.localtime())}.txt'

        if input_area.get_file_path() is None:
            initial_dir = Path.cwd
        else:
            initial_dir = os.path.dirname(input_area.get_file_path())
        file_types = [("テキストファイル", "*.txt")]
        file_path = filedialog.asksaveasfilename(filetypes=file_types, initialdir=initial_dir, initialfile=file_name)
        if file_path == "":
            return False
        if not file_path.endswith(".txt"):
            file_path += ".txt"

        self._backup_file(file_path)
        input_text = input_area.get_text()
        with open(file_path, "w", encoding="utf-8-sig") as f:
            f.write(input_text)
        input_area.set_file(input_text, file_path)
        self.form.update_title()
        self._add_recent_file(file_path)
        return True

    def _backup_file(self, file_path):
        if not os.path.exists(file_path):
            return
        YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        log_file_name = f"{YYYYMMDD_HHMMSS}-{os.path.basename(file_path)}"
        shutil.copy2(file_path, os.path.join(Path.daily_log, log_file_name))

    def save_all_file(self):
        input_area = self.ctx.form.input_area
        init_tab = input_area.tab
        for tab in input_area.tabs:
            input_area.select_tab(tab)
            self.save_file()
        input_area.select_tab(init_tab)

    def close_file(self):
        input_area = self.ctx.form.input_area
        if not self.ask_save():
            return
        input_area.close_tab()
        self.form.update_title()

    def close_all_file(self):
        input_area = self.ctx.form.input_area

        for tab in reversed(input_area.tabs):
            input_area.select_tab(tab)
            self.close_file()

    def ask_save(self, func=None):
        input_area = self.ctx.form.input_area

        input_text = input_area.get_text()
        if input_area.get_file_text() == input_text:
            return True
        result = messagebox.askyesnocancel("EasyNovelAssistant", "変更内容を保存しますか？")
        if result is None:
            return False
        if result:
            if func is None:
                func = self.save_file
            return func()
        return True
