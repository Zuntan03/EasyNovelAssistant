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

        descs = [  # TODO: set or insert
            # {"label": "チュートリアル", "path": "tutorial.json"},
            {"label": "サンプル", "path": "sample.json"},
            {"label": "NSFW サンプル", "path": "nsfw.json"},  # 特殊
            # テンプレ
        ]

        for desc in descs:
            menu = tk.Menu(form.win, tearoff=False)
            form.menu_bar.add_cascade(label=desc["label"], menu=menu)

            menu.configure(postcommand=lambda mn=menu, ds=desc: self.on_menu_open(mn, ds))

    def on_menu_open(self, menu, desc):
        menu.delete(0, tk.END)

        func = self.ctx.input_area.set_text  # TODO: ラベルでappend差し替え

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
        func(value)
