@echo off
chcp 65001 > NUL

if not exist %~dp0..\..\Style-Bert-VITS2 (
	echo [Error] Style-Bert-VITS2 がインストールされていません。
	pause & exit /b 1
)

pushd %~dp0..\..\Style-Bert-VITS2

call %~dp0ActivateVirtualEnvironment.bat
if %errorlevel% neq 0 ( popd & exit /b 1 )

@REM --cpu
echo python server_fastapi.py %*
python server_fastapi.py %*
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

popd
