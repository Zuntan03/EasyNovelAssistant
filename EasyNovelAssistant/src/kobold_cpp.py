import json
import os
import subprocess
from sys import platform

import requests
from path import Path


class KoboldCpp:
    BAT_TEMPLATE = """@echo off
chcp 65001 > NUL
pushd %~dp0
set CURL_CMD=C:\Windows\System32\curl.exe --ssl-no-revoke

set GPU_LAYERS=0
set CONTEXT_SIZE={context_size}

{curl_cmd}
koboldcpp.exe --gpulayers %GPU_LAYERS% {option} --contextsize %CONTEXT_SIZE% {file_name}
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )
popd
"""

    CURL_TEMPLATE = """if not exist {file_name} (
    %CURL_CMD% -LO {url}
)
"""

    def __init__(self, ctx):
        self.ctx = ctx
        self.base_url = f'http://{ctx["koboldcpp_host"]}:{ctx["koboldcpp_port"]}'
        self.model_url = f"{self.base_url}/api/v1/model"
        self.generate_url = f"{self.base_url}/api/v1/generate"
        self.check_url = f"{self.base_url}/api/extra/generate/check"
        self.abort_url = f"{self.base_url}/api/extra/abort"

        self.model_name = None

        for llm_name in ctx.llm:
            llm = ctx.llm[llm_name]
            llm["name"] = llm_name
            llm["file_names"] = []
            for url in llm["urls"]:
                llm["file_names"].append(url.split("/")[-1])
            llm["file_name"] = llm["file_names"][0]

            bat_file = os.path.join(Path.kobold_cpp, f"Run-{llm_name}-L0.bat")
            if not os.path.exists(bat_file):
                curl_cmd = ""
                for url in llm["urls"]:
                    curl_cmd += self.CURL_TEMPLATE.format(url=url, file_name=url.split("/")[-1])
                bat_text = self.BAT_TEMPLATE.format(
                    curl_cmd=curl_cmd,
                    option=ctx["koboldcpp_arg"],
                    context_size=llm["context_size"],
                    file_name=llm["file_name"],
                )
                with open(bat_file, "w", encoding="utf-8") as f:
                    f.write(bat_text)

    def get_model(self):
        try:
            response = requests.get(self.model_url, timeout=self.ctx["koboldcpp_command_timeout"])
            if response.status_code == 200:
                self.model_name = response.json()["result"].split("/")[-1]
                return self.model_name
        except Exception as e:
            pass
        self.model_name = None
        return self.model_name

    def get_instruct_sequence(self):
        if self.model_name is not None:
            for key in self.ctx.llm_sequence.keys():
                if key in self.model_name:
                    return self.ctx.llm_sequence[key]["instruct"]
        return None

    def get_stop_sequence(self):
        if self.model_name is not None:
            for key in self.ctx.llm_sequence.keys():
                if key in self.model_name:
                    return self.ctx.llm_sequence[key]["stop"]
        return []

    def download_model(self, llm_name):
        llm = self.ctx.llm[llm_name]
        for url in llm["urls"]:
            curl_cmd = f"curl --ssl-no-revoke -LO {url}"
            if subprocess.run(curl_cmd, shell=True, cwd=Path.kobold_cpp).returncode != 0:
                print(f"{llm_name} のダウンロードに失敗しました。\n{curl_cmd}")
                return False
        return True

    def launch_server(self):
        loaded_model = self.get_model()
        if loaded_model is not None:
            print(f"{loaded_model} がすでにロード済みです。\nモデルのサーバーを終了してからロードしてください。")
            return

        llm_name = self.ctx["llm_name"]
        gpu_layer = self.ctx["llm_gpu_layer"]
        llm = self.ctx.llm[llm_name]
        llm_path = os.path.join(Path.kobold_cpp, llm["file_name"])

        if not os.path.exists(llm_path):
            if not self.download_model(llm_name):
                return

        if not os.path.exists(llm_path):
            print(f"{llm_path} がありません。")
            return

        command_args = (
            f'{self.ctx["koboldcpp_arg"]} --gpulayers {gpu_layer} --contextsize {llm["context_size"]} {llm_path}'
        )
        if platform == "win32":
            command = ["start", f"{llm_name} L{gpu_layer}", "cmd", "/c"]
            command.append(f"{Path.kobold_cpp_win} {command_args} || pause")
            subprocess.run(command, shell=True)
        else:
            subprocess.Popen(f"{Path.kobold_cpp_linux} {command_args}", shell=True)

    def generate(self, text):
        ctx = self.ctx
        llm_name = ctx["llm_name"]
        llm = ctx.llm[llm_name]

        args = {
            "max_context_length": llm["context_size"],
            "max_length": ctx["max_length"],
            "prompt": text,
            "quiet": False,
            "stop_sequence": self.get_stop_sequence(),
            "rep_pen": ctx["rep_pen"],
            "rep_pen_range": ctx["rep_pen_range"],
            "rep_pen_slope": ctx["rep_pen_slope"],
            "temperature": ctx["temperature"],
            "tfs": ctx["tfs"],
            "top_a": ctx["top_a"],
            "top_k": ctx["top_k"],
            "top_p": ctx["top_p"],
            "typical": ctx["typical"],
            "min_p": ctx["min_p"],
            "sampler_order": ctx["sampler_order"],
        }

        try:
            response = requests.post(self.generate_url, json=args)
            if response.status_code == 200:
                if self.model_name is not None:
                    args["model_name"] = self.model_name
                args["result"] = response.json()["results"][0]["text"]
                with open(Path.generate_log, "a", encoding="utf-8-sig") as f:
                    json.dump(args, f, indent=4, ensure_ascii=False)
                    f.write("\n")
                return args["result"]
            print(response.text)
        except Exception as e:
            print(e)
        return None

    def check(self):
        try:
            response = requests.get(self.check_url)
            if response.status_code == 200:
                return response.json()["results"][0]["text"]
            print(response.text)
        except Exception as e:
            print(e)
        return None

    def abort(self):
        try:
            response = requests.post(self.abort_url, timeout=self.ctx["koboldcpp_command_timeout"])
            if response.status_code == 200:
                return response.json()["success"]
            print(response.text)
        except Exception as e:
            print(e)
        return None
