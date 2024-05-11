import json
import os

from path import Path


class Context:
    def __init__(self):
        self.cfg = None
        self.llm = None
        self.llm_sequence = None
        self._load_config()

    def _load_config(self):
        assert os.path.exists(Path.default_config)
        with open(Path.default_config, "r", encoding="utf-8-sig") as f:
            self.cfg = json.load(f)
        if os.path.exists(Path.config):
            with open(Path.config, "r", encoding="utf-8-sig") as f:
                self.cfg.update(json.load(f))
        else:
            with open(Path.config, "w", encoding="utf-8-sig") as f:
                json.dump(self.cfg, f, indent=4, ensure_ascii=False)

        with open(Path.default_llm, "r", encoding="utf-8-sig") as f:
            self.llm = json.load(f)
        if os.path.exists(Path.llm):
            with open(Path.llm, "r", encoding="utf-8-sig") as f:
                self.llm.update(json.load(f))
        else:
            with open(Path.llm, "w", encoding="utf-8-sig") as f:
                f.write("{}")

        with open(Path.default_llm_sequence, "r", encoding="utf-8-sig") as f:
            self.llm_sequence = json.load(f)
        if os.path.exists(Path.llm_sequence):
            with open(Path.llm_sequence, "r", encoding="utf-8-sig") as f:
                self.llm_sequence.update(json.load(f))
        else:
            with open(Path.llm_sequence, "w", encoding="utf-8-sig") as f:
                f.write("{}")

    def __getitem__(self, item):
        return self.cfg.get(item, None)

    def __setitem__(self, key, value):
        self.cfg[key] = value

    def finalize(self):
        if not self.form.file_menu.ask_save():  # TODO: すべて閉じる
            return
        self.form.update_config()

        with open(Path.config, "w", encoding="utf-8-sig") as f:
            json.dump(self.cfg, f, indent=4, ensure_ascii=False)

        self.form.win.destroy()

        if self.generator.enabled:
            self.kobold_cpp.abort()
