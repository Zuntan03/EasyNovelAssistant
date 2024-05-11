import time

from const import Const
from context import Context
from form import Form
from generator import Generator
from kobold_cpp import KoboldCpp
from movie_maker import MovieMaker
from path import Path
from style_bert_vits2 import StyleBertVits2


class EasyNovelAssistant:
    SLEEP_TIME = 50

    def __init__(self):
        self.ctx = Context()
        Path.init(self.ctx)
        Const.init(self.ctx)

        self.ctx.kobold_cpp = KoboldCpp(self.ctx)
        self.ctx.style_bert_vits2 = StyleBertVits2(self.ctx)
        self.ctx.movie_maker = MovieMaker(self.ctx)
        self.ctx.form = Form(self.ctx)
        self.ctx.generator = Generator(self.ctx)

        # TODO: 起動時引数でのフォルダ・ファイル読み込み
        self.ctx.form.input_area.open_tab(self.ctx["input_text"])  # 書き出しは Form の finalize

        self.ctx.form.win.after(self.SLEEP_TIME, self.mainloop)

    def run(self):
        self.ctx.form.run()

    def mainloop(self):
        self.ctx.generator.update()
        self.ctx.style_bert_vits2.update()
        self.ctx.form.input_area.update()
        self.ctx.form.win.after(self.SLEEP_TIME, self.mainloop)


if __name__ == "__main__":
    easy_novel_assistant = EasyNovelAssistant()
    easy_novel_assistant.run()
