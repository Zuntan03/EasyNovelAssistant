import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext

from const import Const
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class FileWatcher(FileSystemEventHandler):
    def __init__(self, parent, target_path):
        self.parent = parent
        self.target_path = target_path
        self.abs_path = os.path.abspath(target_path)

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.abs_path:
            self.parent.open_request = self.target_path


class InputTab:
    INTRO_PREFIX = "// intro\n"

    def __init__(self, ctx, notebook, file_text, file_path):
        self.ctx = ctx
        self.notebook = notebook

        self.observer = None
        self.watcher = None
        self.open_request = None

        self.text_area = scrolledtext.ScrolledText(self.notebook, undo=True, maxundo=-1)
        self.text_area.configure(Const.TEXT_AREA_CONFIG)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self._apply_text_setting()
        self.text_area.bind("<KeyRelease>", lambda e: self._update_title())

        self.file_text = ""
        if file_text is not None:
            self.file_text = file_text
            self._set_text(file_text)

        self.file_path = file_path
        self.notebook.add(self.text_area)
        self._update_title()

        self.ctx_menu = tk.Menu(self.text_area, tearoff=False)
        self.text_area.bind("<Button-3>", self._on_ctx_menu)
        self.text_area.bind("<Button-2>", self._on_middle_click)

        self.notebook.select(self.text_area)

    def _update_title(self):
        title = "無題"
        if self.file_path is not None:
            title = os.path.splitext(os.path.basename(self.file_path))[0]

        if self.file_text != self._get_text():
            title += " *"

        if self._is_intro():
            title = "(i) " + title

        self.notebook.tab(self.text_area, text=title)

    def _apply_text_setting(self):
        self.text_area.configure(font=(self.ctx["text_area_font"], self.ctx["text_area_font_size"]))
        colors = {
            "fg": self.ctx["foreground_color"],
            "bg": self.ctx["background_color"],
            "selectforeground": self.ctx["select_foreground_color"],
            "insertbackground": self.ctx["select_foreground_color"],
            "selectbackground": self.ctx["select_background_color"],
        }
        self.text_area.configure(colors)

    def _on_middle_click(self, e):
        if self.ctx["middle_click_speech"]:
            self._speech(e)
        return "break"

    def _on_ctx_menu(self, e):
        self.ctx_menu.delete(0, tk.END)

        if self.ctx.style_bert_vits2.models is None:
            self.ctx.style_bert_vits2.get_models()

        if self.ctx.style_bert_vits2.models is not None:
            self.ctx_menu.add_command(label="読み上げる", command=lambda: self._speech(e))
            self.ctx_menu.add_separator()

        sequence = self.ctx.kobold_cpp.get_instruct_sequence()
        if sequence is not None:
            self.ctx_menu.add_command(label="指示タグを挿入", command=self._insert_instruct_tag)
            self.ctx_menu.add_separator()

        def edit_undo():
            self.text_area.edit_undo()
            self._update_title()

        def edit_redo():
            self.text_area.edit_redo()
            self._update_title()

        def edit_clear():
            self.text_area.delete("1.0", tk.END)
            self._update_title()

        self.ctx_menu.add_command(label="元に戻す (Ctrl+Z)", command=edit_undo)
        self.ctx_menu.add_command(label="やり直し (Ctrl+Y)", command=edit_redo)
        self.ctx_menu.add_separator()

        self.ctx_menu.add_command(label="クリア", command=edit_clear)

        self.text_area.mark_set(tk.INSERT, f"@{e.x},{e.y}")
        self.ctx_menu.post(e.x_root, e.y_root)

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
        self._update_title()

    def _set_text(self, text):
        self.text_area.delete("1.0", tk.END)
        self._append_text(text)

    def _append_text(self, text):
        self.text_area.insert(tk.END, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.END)
            self.text_area.mark_set(tk.INSERT, tk.END)

    def _insert_text(self, text):
        self.text_area.insert(tk.INSERT, text)
        if self.ctx["auto_scroll"]:
            self.text_area.see(tk.INSERT)

    def _get_text(self):
        return self.text_area.get("1.0", "end-1c")

    def _get_comment_removed_text(self):
        text = self._get_text()
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

    def _is_intro(self):
        return self._get_text().lower().startswith(self.INTRO_PREFIX)

    def _switch_intro(self):
        text = self._get_text()
        if text.lower().startswith(self.INTRO_PREFIX):
            self._set_text(text[len(self.INTRO_PREFIX) :])
        else:
            self._set_text(self.INTRO_PREFIX + text)

    def _update(self):
        if self.ctx["watch_file"]:
            if (self.watcher is not None) and (self.watcher.target_path != self.file_path):
                self.observer.stop()
                self.observer.join()
                self.observer = None
                self.watcher = None
                self.open_request = None

            if (self.observer is None) and (self.file_path is not None) and (os.path.exists(self.file_path)):
                self.watcher = FileWatcher(self, self.file_path)
                self.observer = Observer()
                self.observer.schedule(self.watcher, os.path.dirname(self.file_path), recursive=False)
                self.open_request = None
                self.observer.start()

            if self.open_request is not None:
                self.ctx.form.file_menu._open_file(self.open_request, self.ctx.form.file_menu.save_as_file)
                self.open_request = None
        else:
            if self.observer is not None:
                self.observer.stop()
                self.observer.join()
                self.observer = None
                self.watcher = None
                self.open_request = None


class InputArea:
    def __init__(self, parent, ctx):
        self.ctx = ctx
        self.notebook = ttk.Notebook(parent)
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)
        self.notebook.bind("<Button-2>", self._on_middle_click)
        self.ctx_menu = tk.Menu(parent, tearoff=False)
        self.notebook.bind("<Button-3>", self._on_ctx_menu)

        parent.add(self.notebook, width=ctx["input_area_width"], minsize=Const.AREA_MIN_SIZE, stretch="always")

        self.tabs = []
        self.tab = None

    def _on_ctx_menu(self, e):
        self.ctx_menu.delete(0, tk.END)
        try:
            tab_index = self.notebook.index("@%d,%d" % (e.x, e.y))
        except tk.TclError:
            return "break"

        self.notebook.select(tab_index)
        current_tab = self.tabs[tab_index]

        def switch_intro():
            current_tab._switch_intro()
            current_tab._update_title()

        intro_var = tk.BooleanVar(value=current_tab._is_intro())
        self.ctx_menu.add_checkbutton(label="イントロプロンプト", variable=intro_var, command=switch_intro)

        self.ctx_menu.add_separator()

        def copy_tab():
            # 末尾以外なら tabs と notebook の同期必要
            self.open_tab(current_tab._get_text(), None)

        self.ctx_menu.add_command(label="タブを複製", command=copy_tab)

        self.ctx_menu.add_separator()

        def close_right():
            for tab in reversed(self.tabs[tab_index + 1 :]):
                self.select_tab(tab)
                self.ctx.form.file_menu.close_file()

        self.ctx_menu.add_command(label="右側を閉じる", command=close_right)

        def close_others():
            for tab in reversed(self.tabs):
                if tab == current_tab:
                    continue
                self.select_tab(tab)
                self.ctx.form.file_menu.close_file()

        self.ctx_menu.add_command(label="他を閉じる", command=close_others)

        # 閉じる
        self.ctx_menu.add_command(label="閉じる", command=lambda: self.ctx.form.file_menu.close_file())

        self.ctx_menu.post(e.x_root, e.y_root)
        return "break"

    def _on_middle_click(self, e):
        try:
            tab_index = self.notebook.index("@%d,%d" % (e.x, e.y))
        except tk.TclError:
            return "break"
        self.notebook.select(tab_index)
        self.ctx.form.file_menu.close_file()
        return "break"

    def _on_tab_changed(self, e):
        self.tab = self.tabs[self.notebook.index("current")]
        self.ctx.form.update_title()

    def open_tab(self, text=None, path=None):
        # パスが一致するタブがあれば再利用
        if path is not None:
            for tab in self.tabs:
                if tab.file_path == path:
                    self.select_tab(tab)
                    self.set_text(text)
                    self.set_file(text, path)
                    tab._update_title()
                    return

        self.tab = InputTab(self.ctx, self.notebook, text, path)
        self.tabs.append(self.tab)

    def close_tab(self, safety=True):
        self.tabs.remove(self.tab)
        self.notebook.forget(self.tab.text_area)
        self.tab = None
        if len(self.tabs) > 0:
            self.tab = self.tabs[-1]
            self.notebook.select(self.tab.text_area)
        else:
            if safety:
                self.open_tab()

    def select_tab(self, tab):
        self.tab = tab
        self.notebook.select(tab.text_area)

    def close_unmodified_new_tab(self):
        if (self.tab.file_path is None) and (self.tab.file_text == self.tab._get_text()):
            self.close_tab(False)

    def apply_text_setting(self):
        for tab in self.tabs:
            tab._apply_text_setting()

    def set_text(self, text):
        self.tab._set_text(text)

    def get_file_path(self):
        return self.tab.file_path

    def get_file_text(self):
        return self.tab.file_text

    def set_file(self, file_text, file_path):
        self.tab.file_text = file_text
        self.tab.file_path = file_path
        self.tab._update_title()

    def append_text(self, text):
        self.tab._append_text(text)

    def insert_text(self, text):
        self.tab._insert_text(text)

    def get_text(self):
        return self.tab._get_text()

    def get_comment_removed_text(self):
        return self.tab._get_comment_removed_text()

    def get_prompt_text(self):
        text = ""
        for tab in self.tabs:
            if tab == self.tab:
                continue
            if tab._is_intro():
                text += tab._get_comment_removed_text()
        text += self.get_comment_removed_text()
        return text

    def update(self):
        for tab in self.tabs:
            tab._update()
