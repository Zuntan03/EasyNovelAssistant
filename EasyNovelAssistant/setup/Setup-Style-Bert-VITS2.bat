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

echo pip install -qq -r requirements.txt
pip install -qq -r requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo python initialize.py
python initialize.py
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

if not exist Server_cpu.bat (
	echo copy %~dp0res\Server_cpu.bat .
	copy %~dp0res\Server_cpu.bat .
)

if not exist model_assets\Rinne ( mkdir model_assets\Rinne )

setlocal enabledelayedexpansion
if not exist model_assets\Rinne\Rinne.safetensors (
	echo %CURL_CMD% -Lo model_assets\Rinne\Rinne.safetensors https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/Rinne.safetensors
	%CURL_CMD% -Lo model_assets\Rinne\Rinne.safetensors https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/Rinne.safetensors
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist model_assets\Rinne\config.json (
	echo %CURL_CMD% -Lo model_assets\Rinne\config.json https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/config.json
	%CURL_CMD% -Lo model_assets\Rinne\config.json https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/config.json
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if not exist model_assets\Rinne\style_vectors.npy (
	echo %CURL_CMD% -Lo model_assets\Rinne\style_vectors.npy https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/style_vectors.npy
	%CURL_CMD% -Lo model_assets\Rinne\style_vectors.npy https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2/resolve/main/model_assets/Rinne/style_vectors.npy
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)
endlocal

if not exist config.yml (
	echo copy %~dp0res\config.yml .
	copy %~dp0res\config.yml .
)

popd
