import tkinter as tk
from tkinter import simpledialog


class SettingMenu:

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="設定", menu=self.menu)
        self.menu.configure(postcommand=self._on_menu_open)

    def _on_menu_open(self):
        self.menu.delete(0, tk.END)

        cmd = lambda: self._set_name("char_name", "キャラ名")
        self.menu.add_command(label=f'キャラ名: {self.ctx["char_name"]}', command=cmd)

        cmd = lambda: self._set_name("user_name", "ユーザー名")
        self.menu.add_command(label=f'ユーザー名: {self.ctx["user_name"]}', command=cmd)

    def _set_name(self, who, who_label):
        name = self.ctx[who]

        name = simpledialog.askstring(
            f"{who_label}設定",
            f"サンプルなどで使用する{who_label}を入力してください。",
            initialvalue=name,
            parent=self.form.win,
        )
        if name is None:
            return
        elif name != "":
            self.ctx[who] = name
