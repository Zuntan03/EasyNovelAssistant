import tkinter as tk
from tkinter import scrolledtext

from const import Const


class InputArea:
    def __init__(self, parent, ctx):
        self.ctx = ctx
        self.text_area = scrolledtext.ScrolledText(parent, undo=True, maxundo=-1)
        self.text_area.configure(Const.TEXT_AREA_CONFIG)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        parent.add(self.text_area, width=ctx["input_area_width"], minsize=Const.AREA_MIN_SIZE, stretch="always")

        self.ctx_menu = tk.Menu(self.text_area, tearoff=False)
        self.text_area.bind("<Button-3>", self._on_ctx_menu)

        self.text_area.bind("<Button-2>", self._on_middle_click)

    def set_text(self, text):
        self.text_area.delete("1.0", tk.END)
        self.append_text(text)

    def append_text(self, text):
        self.text_area.insert(tk.END, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.END)
            self.text_area.mark_set(tk.INSERT, tk.END)

    def insert_text(self, text):
        self.text_area.insert(tk.INSERT, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.INSERT)

    def get_text(self):
        return self.text_area.get("1.0", "end-1c")

    def get_comment_removed_text(self):
        text = self.get_text()
        lines = text.splitlines()
        new_lines = []
        for line in lines:
            if line.startswith("//"):
                continue
            new_lines.append(line)
        result = "\n".join(new_lines)
        if text.endswith("\n"):  # splitlines は末尾改行を無視するため
            result += "\n"
        return result

    def _speech(self, e):
        line_num = self.text_area.index(f"@{e.x},{e.y}").split(".")[0]
        text = self.text_area.get(f"{line_num}.0", f"{line_num}.end") + "\n"
        self.ctx.style_bert_vits2.generate(text)

    def _insert_instruct_tag(self):
        sequence = self.ctx.kobold_cpp.get_instruct_sequence()
        if sequence is None:
            return
        if self.text_area.tag_ranges(tk.SEL):
            sequence = sequence.format(self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST))
            self.text_area.replace(tk.SEL_FIRST, tk.SEL_LAST, sequence)
        else:
            self.text_area.insert(tk.INSERT, sequence.format(""))

    def _on_middle_click(self, e):
        if self.ctx["middle_click_speech"]:
            self._speech(e)
        return "break"

    def _on_ctx_menu(self, event):
        self.ctx_menu.delete(0, tk.END)

        if self.ctx.style_bert_vits2.models is None:
            self.ctx.style_bert_vits2.get_models()

        if self.ctx.style_bert_vits2.models is not None:
            self.ctx_menu.add_command(label="読み上げる", command=lambda: self._speech(event))

        sequence = self.ctx.kobold_cpp.get_instruct_sequence()
        if sequence is not None:
            self.ctx_menu.add_command(label="指示タグを挿入", command=self._insert_instruct_tag)
            self.ctx_menu.add_separator()

        self.ctx_menu.add_command(label="元に戻す (Ctrl+Z)", command=self.text_area.edit_undo)
        self.ctx_menu.add_command(label="やり直し (Ctrl+Y)", command=self.text_area.edit_redo)
        self.ctx_menu.add_separator()

        self.ctx_menu.add_command(label="クリア", command=lambda: self.text_area.delete("1.0", tk.END))

        self.text_area.mark_set(tk.INSERT, f"@{event.x},{event.y}")
        self.ctx_menu.post(event.x_root, event.y_root)
