import tkinter as tk


class Const:
    AREA_MIN_SIZE = 128

    @classmethod
    def init(cls, ctx):
        cls.TEXT_AREA_CONFIG = {
            "spacing1": 4,
            "spacing2": 4,
            "spacing3": 4,
            "wrap": tk.CHAR,
        }
