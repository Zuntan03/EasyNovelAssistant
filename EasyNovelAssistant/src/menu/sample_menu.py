import json
import os
import tkinter as tk
import urllib.request
import webbrowser
from urllib.parse import quote

from path import Path


class SampleMenu:
    URL_TEMPLATE = "https://yyy.wpx.jp/EasyNovelAssistant/sample/{0}"

    def __init__(self, form, ctx):
        self.form = form
        self.ctx = ctx

        descs = [
            {
                "label": "テンプレート",
                "mode": "insert",
                "path": "template.json",
                "splitter_names": ["画像生成用プロンプト（実験的）"],
            },
            {"label": "サンプル", "mode": "set", "path": "sample.json", "splitter_names": []},
            {
                "label": "NSFW サンプル",
                "mode": "set",
                "path": "nsfw.json",
                "splitter_names": ["ボーイズラブ、ファンタジー、悪魔、美形", "妄想ジェネレーター"],
            },
            {
                "label": "読み上げサンプル",
                "mode": "set",
                "path": "speech.json",
                "splitter_names": [],
            },
        ]

        for desc in descs:
            menu = tk.Menu(form.win, tearoff=False)
            form.menu_bar.add_cascade(label=desc["label"], menu=menu)

            menu.configure(postcommand=lambda mn=menu, ds=desc: self.on_menu_open(mn, ds))

    def on_menu_open(self, menu, desc):
        menu.delete(0, tk.END)

        func = self.ctx.input_area.set_text
        if desc["mode"] == "insert":
            func = self.ctx.input_area.insert_text

        categories = {}

        json_path = os.path.join(Path.sample, desc["path"])
        dic = None
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8-sig") as f:
                dic = json.load(f)

        if dic is None:
            menu.add_command(label=f'{desc["label"]} をダウンロード', command=lambda p=desc["path"]: self._download(p))
            return

        for key in dic:
            name = key
            if "/" in name:
                category, name = name.split("/")
                if category not in categories:
                    categories[category] = tk.Menu(menu, tearoff=False)
                    menu.add_cascade(label=category, menu=categories[category])
                categories[category].add_command(
                    label=name, command=lambda v=dic[key], f=func: self.on_menu_select(v, f)
                )
            else:
                menu.add_command(label=name, command=lambda v=dic[key], f=func: self.on_menu_select(v, f))

            if name in desc["splitter_names"]:
                menu.add_separator()

    def _download(self, path):
        url = self.URL_TEMPLATE.format(path)
        try:
            with urllib.request.urlopen(url) as res:
                data = res.read()
            with open(os.path.join(Path.sample, path), "wb") as f:
                f.write(data)
                return data
        except Exception as e:
            print(e)
        return None

    def on_menu_select(self, value, func):
        if value.startswith("http"):
            url = quote(value, safe=":/")
            try:
                with urllib.request.urlopen(url) as res:
                    value = res.read().decode("utf-8-sig")
            except Exception as e:
                webbrowser.open(url)
                print(f"{e}. {url}")
                return
        if ("{char_name}" in value) or ("{user_name}" in value):
            value = value.format(char_name=self.ctx["char_name"], user_name=self.ctx["user_name"])
        func(value)
