@echo off
chcp 65001 > NUL
setlocal

set "HOST=%~1"
if "%HOST%"=="" set "HOST=0.0.0.0"

set "PORT=%~2"
if "%PORT%"=="" set "PORT=8088"

set "CPU_ARG=%~3"

if not exist "%~dp0..\..\Irodori-TTS-Server\" (
	echo [Error] Irodori-TTS-Server is not installed.
	pause & exit /b 1
)

call "%~dp0ActivateVirtualEnvironment.bat" "%~dp0..\..\venv"
if %errorlevel% neq 0 ( exit /b 1 )

pushd "%~dp0..\..\Irodori-TTS-Server"

if /i "%CPU_ARG%"=="--cpu" (
	set "IRODORI_MODEL_DEVICE=cpu"
	set "IRODORI_CODEC_DEVICE=cpu"
)
set "IRODORI_ALLOW_NO_REF_VOICE=true"

echo python -m uv run python -m irodori_openai_tts --host %HOST% --port %PORT%
python -m uv run python -m irodori_openai_tts --host %HOST% --port %PORT%
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

popd
endlocal
exit /b 0
