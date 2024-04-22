import os
import time


class Path:
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
    kobold_cpp_exe = os.path.join(kobold_cpp, "koboldcpp.exe")

    sample = os.path.join(cwd, "sample")

    log = os.path.join(cwd, "log")
    os.makedirs(log, exist_ok=True)
    YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    generate_log = os.path.join(log, f"{YYYYMMDD_HHMMSS}-generate.txt")
    output_log = os.path.join(log, f"{YYYYMMDD_HHMMSS}-output.txt")

    @classmethod
    def init(cls, ctx):
        pass
