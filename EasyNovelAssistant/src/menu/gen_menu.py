import tkinter as tk


class GenMenu:
    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        self.menu = tk.Menu(form.win, tearoff=False)
        self.form.menu_bar.add_cascade(label="生成", menu=self.menu)
        self.menu.configure(postcommand=self.on_menu_open)

        self.form.win.bind("<F3>", lambda e: self._enable())
        self.form.win.bind("<F4>", lambda e: self._disable())
        self.form.win.bind("<Shift-F5>", lambda e: self._set_enabled(not self.ctx.generator.enabled))
        self.form.win.bind("<F5>", lambda e: self._abort())

    def _set_enabled(self, enabled):
        self.ctx.generator.enabled = enabled
        self.ctx.kobold_cpp.get_model()
        self.ctx.form.update_title()
        if not enabled:
            self.ctx.generator.abort()

    def _enable(self):
        if not self.ctx.generator.enabled:
            self._set_enabled(True)

    def _disable(self):
        if self.ctx.generator.enabled:
            self._set_enabled(False)

    def _abort(self):
        self.ctx.generator.abort()
        self.ctx.style_bert_vits2.abort()

    def on_menu_open(self):
        self.menu.delete(0, tk.END)

        self.menu.add_command(label="生成を開始 (F3)", command=self._enable)

        self.menu.add_command(label="生成を終了 (F4)", command=self._disable)

        def set_enabled(*args):
            self._set_enabled(self.enabled_var.get())

        self.enabled_var = tk.BooleanVar(value=self.ctx.generator.enabled)
        self.enabled_var.trace_add("write", set_enabled)
        self.menu.add_checkbutton(label="生成の開始/終了 (Shift+F5)", variable=self.enabled_var)

        self.menu.add_command(label="生成を中断 (F5)", command=self.ctx.generator.abort)

        self.menu.add_separator()

        def set_max_length(max_length):
            self.ctx["max_length"] = max_length

        self.max_length_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label=f'生成文の長さ: {self.ctx["max_length"]}', menu=self.max_length_menu)

        llm = self.ctx.llm[self.ctx["llm_name"]]
        max_context_length = min(llm["context_size"], self.ctx["llm_context_size"])
        for max_length in self.ctx["max_lengths"]:
            if max_length >= max_context_length:
                break
            check_var = tk.BooleanVar(value=self.ctx["max_length"] == max_length)
            self.max_length_menu.add_checkbutton(
                label=max_length, variable=check_var, command=lambda gl=max_length, _=check_var: set_max_length(gl)
            )

        self.temperature_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(
            label=f'ゆらぎ度合い (Temperature): {self.ctx["temperature"]}', menu=self.temperature_menu
        )

        def set_temperature(temperature):
            self.ctx["temperature"] = temperature

        temperatures = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for temperature in temperatures:
            check_var = tk.BooleanVar(value=self.ctx["temperature"] == temperature)
            self.temperature_menu.add_checkbutton(
                label=temperature, variable=check_var, command=lambda t=temperature, _=check_var: set_temperature(t)
            )

        self.menu.add_separator()

        def set_auto_scroll(*args):
            self.ctx["auto_scroll"] = self.auto_scroll_var.get()

        self.auto_scroll_var = tk.BooleanVar(value=self.ctx["auto_scroll"])
        self.auto_scroll_var.trace_add("write", set_auto_scroll)
        self.menu.add_checkbutton(label="自動スクロール", variable=self.auto_scroll_var)
