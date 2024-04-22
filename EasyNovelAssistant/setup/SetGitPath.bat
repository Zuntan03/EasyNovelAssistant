@echo off
chcp 65001 > NUL

where /Q git
if %ERRORLEVEL% equ 0 ( exit /b 0 )
cd > NUL

set PORTABLE_GIT_DIR=%~dp0..\lib\PortableGit
if not exist %PORTABLE_GIT_DIR% (
	echo [Error] git が見つかりませんでした。Git for Windows をインストールしてください。
	start https://gitforwindows.org/
	pause & exit /b 1
)

echo set "PATH=%PORTABLE_GIT_DIR%;%PATH%"
set "PATH=%PORTABLE_GIT_DIR%;%PATH%"

where /Q git
if %ERRORLEVEL% equ 0 ( exit /b 0 )
cd > NUL

echo [Error] git が見つかりませんでした。Git for Windows をインストールしてください。
start https://gitforwindows.org/
pause & exit /b 1
