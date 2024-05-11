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
                "label": "ユーザー",
                "mode": "set",
                "change_mode": {},
                "path": "user.json",
                "splitter_names": [],
            },
            {
                "label": "特集テーマ",
                "mode": "open",
                "change_mode": {
                    "サンプル: ": "set",
                    "テンプレ: ": "set",
                },
                "path": "special.json",
                "splitter_names": ["ゴールシークのリポジトリ"],
            },
            {
                "label": "テンプレート",
                "mode": "insert",
                "change_mode": {},
                "path": "template.json",
                "splitter_names": [],
            },
            {"label": "サンプル", "mode": "set", "change_mode": {}, "path": "sample.json", "splitter_names": []},
            {
                "label": "NSFW サンプル",
                "mode": "set",
                "change_mode": {},
                "path": "nsfw.json",
                "splitter_names": ["妄想ジェネレーター"],
            },
            {
                "label": "読み上げサンプル",
                "mode": "set",
                "change_mode": {},
                "path": "speech.json",
                "splitter_names": [],
            },
            {
                "label": "作例や記事",
                "mode": "open",
                "change_mode": {},
                "path": "url.json",
                "splitter_names": [],
            },
        ]

        for desc in descs:
            json_path = os.path.join(Path.sample, desc["path"])
            if os.path.exists(json_path):
                menu = tk.Menu(form.win, tearoff=False)
                form.menu_bar.add_cascade(label=desc["label"], menu=menu)

                menu.configure(postcommand=lambda mn=menu, ds=desc: self.on_menu_open(mn, ds))

    def on_menu_open(self, menu, desc):
        menu.delete(0, tk.END)

        categories = {}

        json_path = os.path.join(Path.sample, desc["path"])
        dic = None
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8-sig") as f:
                dic = json.load(f)

        # if dic is None:
        #     menu.add_command(label=f'{desc["label"]} をダウンロード', command=lambda p=desc["path"]: self._download(p))
        #     return

        change_mode = desc["change_mode"]
        for key in dic:
            item = dic[key]
            mode = desc["mode"]
            if "mode" in item:
                mode = item["mode"]
            name = key
            if "/" in name:
                category, name = name.split("/")
                for change_name in change_mode:
                    if change_name in name:
                        mode = change_mode[change_name]
                if category not in categories:
                    categories[category] = tk.Menu(menu, tearoff=False)
                    menu.add_cascade(label=category, menu=categories[category])
                categories[category].add_command(label=name, command=lambda i=item, m=mode: self.on_menu_select(i, m))
            else:
                for change_name in change_mode:
                    if change_name in name:
                        mode = change_mode[change_name]
                menu.add_command(label=name, command=lambda i=item, m=mode: self.on_menu_select(i, m))

            if name in desc["splitter_names"]:
                menu.add_separator()

    # def _download(self, path):
    #     url = self.URL_TEMPLATE.format(path)
    #     try:
    #         with urllib.request.urlopen(url) as res:
    #             data = res.read()
    #         with open(os.path.join(Path.sample, path), "wb") as f:
    #             f.write(data)
    #             return data
    #     except Exception as e:
    #         print(e)
    #     return None

    def on_menu_select(self, item, mode):
        if (mode == "set") or (mode == "insert"):
            if item.startswith("http"):
                url = quote(item, safe=":/?=")
                try:
                    with urllib.request.urlopen(url) as res:
                        item = res.read().decode("utf-8-sig")
                except Exception as e:
                    webbrowser.open(url)
                    print(f"{e}. {url}")
                    return
            if ("{char_name}" in item) or ("{user_name}" in item):
                item = item.format(char_name=self.ctx["char_name"], user_name=self.ctx["user_name"])
            if mode == "set":
                self.ctx.form.input_area.set_text(item)
            else:
                self.ctx.form.input_area.insert_text(item)
        elif mode == "open":
            if item.startswith("http"):
                url = quote(item, safe=":/?=")
                webbrowser.open(url)
            else:
                print(f"SampleMenu invalid URL: {mode}, {item}")
        else:
            print(f"SampleMenu unknown mode: {mode}, {item}")
