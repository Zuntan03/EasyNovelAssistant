import time

from const import Const
from context import Context
from form import Form
from generator import Generator
from kobold_cpp import KoboldCpp
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
        self.ctx.form = Form(self.ctx)

        self.ctx.file_menu = self.ctx.form.file_menu
        self.ctx.model_menu = self.ctx.form.model_menu
        self.ctx.gen_menu = self.ctx.form.gen_menu

        self.ctx.input_area = self.ctx.form.input_area
        self.ctx.output_area = self.ctx.form.output_area
        self.ctx.gen_area = self.ctx.form.gen_area

        self.ctx.generator = Generator(self.ctx)

        self.ctx.form.win.after(self.SLEEP_TIME, self.mainloop)

    def run(self):
        self.ctx.form.run()

    def mainloop(self):
        self.ctx.generator.update()
        self.ctx.style_bert_vits2.update()
        self.ctx.form.win.after(self.SLEEP_TIME, self.mainloop)


if __name__ == "__main__":
    easy_novel_assistant = EasyNovelAssistant()
    easy_novel_assistant.run()
