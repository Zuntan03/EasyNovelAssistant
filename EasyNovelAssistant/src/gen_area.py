import tkinter as tk
from tkinter import scrolledtext

from const import Const


class GenArea:
    def __init__(self, parent, ctx):
        self.ctx = ctx
        self.text_area = scrolledtext.ScrolledText(parent, state=tk.DISABLED)
        self.text_area.configure(Const.TEXT_AREA_CONFIG)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        parent.add(self.text_area, height=ctx["gen_area_height"], minsize=Const.AREA_MIN_SIZE, stretch="never")

        self.ctx_menu = tk.Menu(self.text_area, tearoff=False)
        self.text_area.bind("<Button-3>", self._on_ctx_menu)

        self.text_area.bind("<Button-2>", self._on_middle_click)

    def set_text(self, text):
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.END)
        self.text_area.configure(state=tk.DISABLED)

    def append_text(self, text):
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.insert(tk.END, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.END)
        self.text_area.configure(state=tk.DISABLED)

    def _on_middle_click(self, e):
        text = None
        if self.text_area.tag_ranges(tk.SEL):
            text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        else:
            line_num = self.text_area.index(f"@{e.x},{e.y}").split(".")[0]
            text = self.text_area.get(f"{line_num}.0", f"{line_num}.end") + "\n"
            # text_area の座標を取得
            # selected_text に text_area を中クリックした行のテキストを代入

        self.ctx.input_area.insert_text(text)
        return "break"

    def _on_ctx_menu(self, event):
        self.ctx_menu.delete(0, tk.END)

        self.ctx_menu.add_command(label="入力欄に送る", command=lambda: self._on_middle_click(None))

        self.text_area.mark_set(tk.INSERT, f"@{event.x},{event.y}")
        self.ctx_menu.post(event.x_root, event.y_root)
