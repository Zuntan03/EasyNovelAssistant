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
