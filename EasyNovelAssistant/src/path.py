import os
import re
import time


class Path:
    path_regex = re.compile(r'[\n\r<>:"/\\|?* ]')

    cwd = os.getcwd()
    config = os.path.join(cwd, "config.json")
    llm = os.path.join(cwd, "llm.json")
    llm_sequence = os.path.join(cwd, "llm_sequence.json")

    app = os.path.join(cwd, "EasyNovelAssistant")
    setup = os.path.join(app, "setup")
    res = os.path.join(setup, "res")
    default_config = os.path.join(res, "default_config.json")
    default_llm = os.path.join(res, "default_llm.json")
    default_llm_sequence = os.path.join(res, "default_llm_sequence.json")

    kobold_cpp = os.path.join(cwd, "KoboldCpp")
    kobold_cpp_win = os.path.join(kobold_cpp, "koboldcpp.exe")
    kobold_cpp_linux = os.path.join(kobold_cpp, "koboldcpp-linux-x64")

    style_bert_vits2 = os.path.join(cwd, "Style-Bert-VITS2")
    style_bert_vits2_config = os.path.join(style_bert_vits2, "config.yml")
    style_bert_vits2_setup = os.path.join(setup, "Setup-Style-Bert-VITS2.bat")
    style_bert_vits2_run = os.path.join(setup, "Run-Style-Bert-VITS2.bat")

    sample = os.path.join(cwd, "sample")

    YYYYMMDD = time.strftime("%Y%m%d", time.localtime())

    log = os.path.join(cwd, "log")
    log_date = os.path.join(log, YYYYMMDD)
    os.makedirs(log_date, exist_ok=True)

    YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    generate_log = os.path.join(log_date, f"{YYYYMMDD_HHMMSS}-generate.txt")
    output_log = os.path.join(log_date, f"{YYYYMMDD_HHMMSS}-output.txt")

    speech = os.path.join(cwd, "speech")
    speech_date = os.path.join(speech, YYYYMMDD)

    @classmethod
    def init(cls, ctx):
        pass

    @classmethod
    def get_path_name(cls, name):
        return cls.path_regex.sub("_", name).replace("___", "_").replace("__", "_")
