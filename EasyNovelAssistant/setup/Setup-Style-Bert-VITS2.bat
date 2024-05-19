@echo off
chcp 65001 > NUL
set CURL_CMD=C:\Windows\System32\curl.exe -k
set PS_CMD=PowerShell -Version 5.1 -ExecutionPolicy Bypass

echo call %~dp0SetGitPath.bat
call %~dp0SetGitPath.bat
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

pushd %~dp0..\..
setlocal enabledelayedexpansion

if exist Style-Bert-VITS2\ (
	echo git -C Style-Bert-VITS2 pull
	git -C Style-Bert-VITS2 pull
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
) else (
	echo git clone https://github.com/litagin02/Style-Bert-VITS2
	git clone https://github.com/litagin02/Style-Bert-VITS2
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

set LIB_DIR=%~dp0lib
if not exist %LIB_DIR%\ ( mkdir %LIB_DIR% )
set FFMPEG_DIR=%LIB_DIR%\ffmpeg-master-latest-win64-gpl

if not exist %FFMPEG_DIR%\ (
	echo %CURL_CMD% -Lo %LIB_DIR%\ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
	%CURL_CMD% -Lo %LIB_DIR%\ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )

	echo %PS_CMD% Expand-Archive -Path %LIB_DIR%\ffmpeg.zip -DestinationPath %LIB_DIR% -Force
	%PS_CMD% Expand-Archive -Path %LIB_DIR%\ffmpeg.zip -DestinationPath %LIB_DIR% -Force
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )

	echo del %LIB_DIR%\ffmpeg.zip
	del %LIB_DIR%\ffmpeg.zip
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist venv\Scripts\ffplay.exe (
	echo xcopy /QY %FFMPEG_DIR%\bin\*.exe venv\Scripts\
	xcopy /QY %FFMPEG_DIR%\bin\*.exe venv\Scripts\
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

endlocal
popd

pushd %~dp0..\..\Style-Bert-VITS2

call %~dp0ActivateVirtualEnvironment.bat
if %errorlevel% neq 0 ( popd & exit /b 1 )

echo python -m pip install -q --upgrade pip
python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -q torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

@REM https://fate.5ch.net/test/read.cgi/liveuranus/1711873736/545
@REM Fix https://github.com/litagin02/Style-Bert-VITS2/commit/053a6bf78505e427489e341805442db20400117a
@REM echo pip install -q gradio==4.23.0
@REM pip install -q gradio==4.23.0
@REM if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo pip install -q -r requirements.txt
pip install -q -r requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

@REM ModuleNotFoundError: No module named 'GPUtil'
echo pip install -q GPUtil
pip install -q GPUtil
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo python initialize.py
python initialize.py
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

if not exist Server_cpu.bat (
	echo copy %~dp0res\Server_cpu.bat .
	copy %~dp0res\Server_cpu.bat .
)

call :DL_HF_MODEL RinneAi/Rinne_Style-Bert-VITS2 model_assets/Rinne Rinne Rinne
if %errorlevel% neq 0 ( popd & exit /b 1 )

call :DL_HF_MODEL kaunista/kaunista-style-bert-vits2-models Anneli Anneli Anneli_e116_s32000
if %errorlevel% neq 0 ( popd & exit /b 1 )

call :DL_HF_MODEL kaunista/kaunista-style-bert-vits2-models Anneli-nsfw Anneli-nsfw Anneli-nsfw_e300_s5100
if %errorlevel% neq 0 ( popd & exit /b 1 )

if not exist config.yml (
	echo copy %~dp0res\config.yml .
	copy %~dp0res\config.yml .
)

popd
exit /b 0

:DL_HF_MODEL
set HF_REP=%1
set MODEL_DIR=%2
set MODEL_NAME=%3
set MODEL_SAFETENSORS=%4

if not exist model_assets\%MODEL_NAME% ( mkdir model_assets\%MODEL_NAME% )

setlocal enabledelayedexpansion
if not exist model_assets\%MODEL_NAME%\%MODEL_NAME%.safetensors (
	echo %CURL_CMD% -Lo model_assets\%MODEL_NAME%\%MODEL_NAME%.safetensors https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/%MODEL_SAFETENSORS%.safetensors
	%CURL_CMD% -Lo model_assets\%MODEL_NAME%\%MODEL_NAME%.safetensors https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/%MODEL_SAFETENSORS%.safetensors
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist model_assets\%MODEL_NAME%\config.json (
	echo %CURL_CMD% -Lo model_assets\%MODEL_NAME%\config.json https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/config.json
	%CURL_CMD% -Lo model_assets\%MODEL_NAME%\config.json https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/config.json
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist model_assets\%MODEL_NAME%\style_vectors.npy (
	echo %CURL_CMD% -Lo model_assets\%MODEL_NAME%\style_vectors.npy https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/style_vectors.npy
	%CURL_CMD% -Lo model_assets\%MODEL_NAME%\style_vectors.npy https://huggingface.co/%HF_REP%/resolve/main/%MODEL_DIR%/style_vectors.npy
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)
endlocal

exit /b 0
