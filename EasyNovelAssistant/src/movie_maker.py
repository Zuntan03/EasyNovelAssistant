import os
import re
import subprocess
import time
from tkinter import filedialog

from path import Path


class MovieMaker:
    _SERIF_REGEX = re.compile(r"^[\d_]*-(.+)")

    def __init__(self, ctx):
        self.ctx = ctx
        self.audio_dir = None
        self.image_dir = ""

    def make(self):
        audio_image_sets = self._select_audio_image_sets()
        if len(audio_image_sets) == 0:
            return False

        movie_path = self._select_movie_path()
        if movie_path is None:
            return False

        bat_path = self._prepare(audio_image_sets, movie_path)
        if bat_path is None:
            return False

        subprocess.run(["start", "cmd", "/c", f"{bat_path} || pause"], shell=True, cwd=os.path.dirname(bat_path))
        return True

    def _select_audio_image_sets(self):
        win = self.ctx.form.win
        result = []

        if self.audio_dir is None:
            if os.path.exists(Path.daily_speech):
                self.audio_dir = Path.daily_speech
            elif os.path.exists(Path.speech):
                self.audio_dir = Path.speech
            else:
                self.audio_dir = Path.cwd

        image_dir = self.ctx["mov_image_dir"]
        if image_dir == "":
            image_dir = Path.cwd

        while True:
            title = "動画にする音声ファイルを選択します。"
            if len(result) > 0:
                title += " [キャンセル] で選択を終了します。"
            audio_path = filedialog.askopenfilename(
                title=title,
                filetypes=[("音声ファイル", "*.wav")],
                initialdir=self.audio_dir,
                parent=win,
            )
            if audio_path == "":
                break
            self.audio_dir = os.path.dirname(audio_path)
            audio_name = os.path.basename(audio_path).split(".")[0]

            image_path = filedialog.askopenfilename(
                title=f"{audio_name} の再生中に表示する画像ファイルを選択します。",
                filetypes=[("画像ファイル", "*.png *.webp *.jpg *.jpeg")],
                initialdir=image_dir,
                parent=win,
            )
            if image_path == "":
                break
            image_dir = os.path.dirname(image_path)
            self.ctx["mov_image_dir"] = image_dir

            result.append({"image_path": image_path, "audio_path": audio_path})

        return result

    def _select_movie_path(self):
        movie_dir = self.ctx["mov_movie_dir"]
        if movie_dir == "":
            movie_dir = Path.movie

        YYYYMMDD_HHMMSS = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        movie_path = filedialog.asksaveasfilename(
            title="動画ファイルを保存",
            filetypes=[("動画ファイル", "*.mp4")],
            initialdir=movie_dir,
            initialfile=f"{YYYYMMDD_HHMMSS}.mp4",
            parent=self.ctx.form.win,
        )
        if movie_path == "":
            return None
        if not movie_path.endswith(".mp4"):
            movie_path += ".mp4"
        self.ctx["mov_movie_dir"] = os.path.dirname(movie_path)
        return movie_path

    def _prepare(self, audio_image_sets, movie_path):
        movie_name = os.path.basename(movie_path).split(".")[0]
        assets_dir = os.path.join(os.path.dirname(movie_path), movie_name)
        os.makedirs(assets_dir, exist_ok=True)

        bat = """@echo off
chcp 65001 > NUL
pushd %~dp0
set FFMPEG={ffmpeg}
set FFPLAY={ffplay}

""".format(
            ffmpeg=Path.ffmpeg, ffplay=Path.ffplay
        )

        subtitle_template = """1
00:00:00,000 --> 90:00:00,000
{serif}
"""
        part_paths = []
        for i, audio_image_set in enumerate(audio_image_sets):
            audio_path = audio_image_set["audio_path"]
            image_path = audio_image_set["image_path"]
            audio_name, _ext = os.path.splitext(os.path.basename(audio_path))
            serif = audio_name
            m = self._SERIF_REGEX.match(audio_name)
            if m is not None:
                serif = m.group(1)
            subtitle = subtitle_template.format(serif=serif)
            subtitle_path = os.path.join(assets_dir, f"{audio_name}.srt")
            with open(subtitle_path, "w", encoding="utf-8-sig") as f:
                f.write(subtitle)

            part_path = os.path.join(assets_dir, f"{audio_name}.mp4")
            part_paths.append(part_path)

            vf = ""
            mov_resize = self.ctx["mov_resize"]
            mov_subtitles = self.ctx["mov_subtitles"]
            if mov_resize > 0 or mov_subtitles:
                vf = '\n-vf "'
                if mov_resize > 0:
                    vf += f"scale='if(gt(a,1),{mov_resize},-2)':'if(gt(a,1),-2,{mov_resize})'"
                    if mov_subtitles:
                        vf += ", "
                if mov_subtitles:
                    vf += f"subtitles='{os.path.basename(subtitle_path)}'"
                vf += '" ^'

            af = ""
            volume_adjust = self.ctx["mov_volume_adjust"]
            tempo_adjust = self.ctx["mov_tempo_adjust"]
            if volume_adjust or tempo_adjust:
                af = '\n-af "'
                if volume_adjust:
                    af += f"volume={self.ctx['speech_volume'] / 100}"
                    if tempo_adjust:
                        af += ", "
                if tempo_adjust:
                    af += f"atempo={self.ctx['speech_speed']}"
                af += '" ^'

            bat += """echo "{i}: {serif}"
%FFMPEG% -y -loglevel error ^
-i "{audio_path}" ^
-loop 1 -i "{image_path}" ^
-vcodec libx264 ^
-pix_fmt yuv420p ^
-acodec aac ^
-ab 128k ^
-ac 1 ^
-ar 44100 ^
-shortest ^{vf}{af}
-crf {crf} ^
"{part_path}"
if %errorlevel% neq 0 ( pause & popd & exit /b 1)

""".format(
                i=i,
                serif=serif,
                audio_path=audio_path,
                image_path=image_path,
                vf=vf,
                af=af,
                crf=self.ctx["mov_crf"],
                part_path=part_path,
            )

        file_list_path = os.path.join(assets_dir, f"{movie_name}.txt")
        with open(file_list_path, "w", encoding="utf-8") as f:
            for part_path in part_paths:
                f.write(f"file '{part_path}'\n")

        bat += """%FFMPEG% -y -loglevel error ^
-f concat ^
-safe 0 ^
-i "{file_list_path}" ^
-c copy ^
"{movie_path}"
if %errorlevel% neq 0 ( pause & popd & exit /b 1)

%FFPLAY% -loglevel error -autoexit -loop 3 "{movie_path}"
if %errorlevel% neq 0 ( pause & popd & exit /b 1)

popd
""".format(
            file_list_path=file_list_path, movie_path=movie_path
        )

        bat_path = os.path.join(assets_dir, f"{movie_name}.bat")
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(bat)
        return bat_path
