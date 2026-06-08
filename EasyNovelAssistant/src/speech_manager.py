STYLE_BERT_VITS2 = "style_bert_vits2"
IRODORI_TTS = "irodori_tts"

SPEECH_ENGINE_LABELS = {
    STYLE_BERT_VITS2: "Style-Bert-VITS2",
    IRODORI_TTS: "Irodori-TTS",
}


def normalize_speech_engine(engine):
    if engine in SPEECH_ENGINE_LABELS:
        return engine
    return STYLE_BERT_VITS2


class SpeechManager:
    def __init__(self, ctx, style_bert_vits2, irodori_tts):
        self.ctx = ctx
        self.style_bert_vits2 = style_bert_vits2
        self.irodori_tts = irodori_tts

    def active_engine(self):
        engine = normalize_speech_engine(self.ctx["speech_engine"])
        if engine != self.ctx["speech_engine"]:
            self.ctx["speech_engine"] = engine
        return engine

    def active_label(self):
        return SPEECH_ENGINE_LABELS[self.active_engine()]

    def active_client(self):
        if self.active_engine() == IRODORI_TTS:
            return self.irodori_tts
        return self.style_bert_vits2

    def get_models(self):
        return self.active_client().get_models()

    @property
    def models(self):
        return self.active_client().models

    def install(self):
        return self.active_client().install()

    def launch_server(self):
        return self.active_client().launch_server()

    def is_installed(self):
        return self.active_client().is_installed()

    def is_installing(self):
        return self.active_client().is_installing()

    def update(self):
        self.style_bert_vits2.update()
        self.irodori_tts.update()

    def abort(self):
        self.style_bert_vits2.abort()
        self.irodori_tts.abort()

    def generate(self, text, force=False):
        return self.active_client().generate(text, force=force)

    def voice_keys(self):
        if self.active_engine() == IRODORI_TTS:
            return ("irodori_char_voice", "irodori_user_voice", "irodori_other_voice")
        return ("char_voice", "user_voice", "other_voice")
