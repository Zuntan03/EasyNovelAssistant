@echo off
chcp 65001 > NUL
pushd %~dp0..\..
set PS_CMD=PowerShell -Version 5.1 -ExecutionPolicy Bypass
set CURL_CMD=C:\Windows\System32\curl.exe -k

set APP_VENV_DIR=venv
set KOBOLD_CPP_DIR=KoboldCpp
set KOBOLD_CPP_EXE=koboldcpp.exe

echo copy /Y %~dp0Install-EasyNovelAssistant.bat Update-EasyNovelAssistant.bat > NUL
copy /Y %~dp0Install-EasyNovelAssistant.bat Update-EasyNovelAssistant.bat > NUL
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

call %~dp0ActivateVirtualEnvironment.bat %APP_VENV_DIR%
if %errorlevel% neq 0 ( popd & exit /b 1 )

echo python -m pip install -q --upgrade pip
python -m pip install -q --upgrade pip

echo python -c "import tkinter" > NUL 2>&1
python -c "import tkinter" > NUL 2>&1
if %errorlevel% neq 0 (
	cd > NUL
	echo %PS_CMD% Expand-Archive -Path %~dp0res\tkinter-PythonSoftwareFoundationLicense.zip -DestinationPath %APP_VENV_DIR% -Force
	%PS_CMD% Expand-Archive -Path %~dp0res\tkinter-PythonSoftwareFoundationLicense.zip -DestinationPath %APP_VENV_DIR% -Force
)

echo pip install -q -r %~dp0res\requirements.txt
pip install -q -r %~dp0res\requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

if not exist %KOBOLD_CPP_DIR%\ ( mkdir %KOBOLD_CPP_DIR% )
popd
pushd %~dp0..\..\%KOBOLD_CPP_DIR%
setlocal enabledelayedexpansion

if not exist koboldcpp.exe (
	echo %CURL_CMD% -LO https://github.com/LostRuins/koboldcpp/releases/latest/download/koboldcpp.exe
	%CURL_CMD% -LO https://github.com/LostRuins/koboldcpp/releases/latest/download/koboldcpp.exe
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist Vecteus-v1-IQ4_XS.gguf (
	echo %CURL_CMD% -LO https://huggingface.co/mmnga/Vecteus-v1-gguf/resolve/main/Vecteus-v1-IQ4_XS.gguf
	%CURL_CMD% -LO https://huggingface.co/mmnga/Vecteus-v1-gguf/resolve/main/Vecteus-v1-IQ4_XS.gguf
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

endlocal
popd
