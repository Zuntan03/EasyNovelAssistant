@echo off
chcp 65001 > NUL
setlocal enabledelayedexpansion

set "BACKEND=%~1"
if "%BACKEND%"=="" set "BACKEND=cu128"

echo call "%~dp0SetGitPath.bat"
call "%~dp0SetGitPath.bat"
if %errorlevel% neq 0 ( pause & exit /b 1 )

pushd "%~dp0..\.."

if exist "Irodori-TTS-Server\" (
	echo git -C Irodori-TTS-Server pull
	git -C Irodori-TTS-Server pull
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
) else (
	echo git clone https://github.com/Aratako/Irodori-TTS-Server
	git clone https://github.com/Aratako/Irodori-TTS-Server
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist "Irodori-TTS-Server\voices\" (
	echo mkdir "Irodori-TTS-Server\voices"
	mkdir "Irodori-TTS-Server\voices"
)

if exist "Irodori-TTS-Server\.env.example" if not exist "Irodori-TTS-Server\.env" (
	echo copy "Irodori-TTS-Server\.env.example" "Irodori-TTS-Server\.env"
	copy "Irodori-TTS-Server\.env.example" "Irodori-TTS-Server\.env"
)

call "%~dp0ActivateVirtualEnvironment.bat" "%~dp0..\..\venv"
if %errorlevel% neq 0 ( popd & exit /b 1 )

pushd "Irodori-TTS-Server"

echo python -m pip install -q --upgrade uv
python -m pip install -q --upgrade uv
if !errorlevel! neq 0 ( pause & popd & popd & exit /b 1 )

echo python -m uv sync --extra %BACKEND%
python -m uv sync --extra %BACKEND%
if !errorlevel! neq 0 ( pause & popd & popd & exit /b 1 )

popd
popd
endlocal
exit /b 0
