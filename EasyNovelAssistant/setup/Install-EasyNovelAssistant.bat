@echo off
chcp 65001 > NUL
set PS_CMD=PowerShell -Version 5.1 -ExecutionPolicy Bypass
set CURL_CMD=C:\Windows\System32\curl.exe

if not exist %CURL_CMD% (
	echo [ERROR] %CURL_CMD% が見つかりません。
	pause & popd & exit /b 1
)

set APP_NAME=EasyNovelAssistant
set APP_NAME_TEMP=%APP_NAME%-temp
set APP_VENV_DIR=venv
set APP_SETUP=%APP_NAME%\setup
set APP_LIB_DIR=%APP_SETUP%\lib
set PORTABLE_GIT_DIR=%~dp0%APP_LIB_DIR%\PortableGit\bin
set PORTABLE_GIT_VER=2.44.0
set CLONE_URL=https://github.com/Zuntan03/EasyNovelAssistant

pushd %~dp0
setlocal enabledelayedexpansion

set "CURRENT_PATH=%CD%"
if "!CURRENT_PATH: =!" neq "%CURRENT_PATH%" (
	echo [ERROR] 現在のフォルダパスにスペースが含まれています。"%CURRENT_PATH%"
	echo スペースを含まないフォルダパスに bat ファイルを移動して、再実行してください。
	pause & popd & exit /b 1
)

if not exist %APP_VENV_DIR%\ (
	echo https://www.python.org
	echo https://github.com/pypa/get-pip
	echo https://github.com/git-for-windows
	echo https://github.com/Zuntan03/EasyNovelAssistant
	echo https://github.com/LostRuins/koboldcpp
	echo https://github.com/litagin02/Style-Bert-VITS2
	echo https://github.com/BtbN/FFmpeg-Builds
	echo.
	echo https://huggingface.co/mmnga/Vecteus-v1-gguf
	echo https://huggingface.co/kaunista/kaunista-style-bert-vits2-models
	echo https://huggingface.co/RinneAi/Rinne_Style-Bert-VITS2
	echo.
	echo "未成年の方はインストール禁止です。"
	echo "以上の配布元から関連ファイルをダウンロードして利用します（URL を Ctrl + クリックで開けます）。"
	echo よろしいですか？ [y/n]
	set /p YES_OR_NO=
	if /i not "!YES_OR_NO!" == "y" ( popd & exit /b 1 )
)

where /Q git
if !errorlevel! neq 0 (
	cd > NUL
	if not exist %PORTABLE_GIT_DIR% (
		if not exist %APP_LIB_DIR%\ ( mkdir %APP_LIB_DIR% )

		echo %CURL_CMD% -k -Lo %APP_LIB_DIR%\PortableGit.7z.exe https://github.com/git-for-windows/git/releases/download/v%PORTABLE_GIT_VER%.windows.1/PortableGit-%PORTABLE_GIT_VER%-64-bit.7z.exe
		%CURL_CMD% -k -Lo %APP_LIB_DIR%\PortableGit.7z.exe https://github.com/git-for-windows/git/releases/download/v%PORTABLE_GIT_VER%.windows.1/PortableGit-%PORTABLE_GIT_VER%-64-bit.7z.exe
		if !errorlevel! neq 0 ( pause & popd & exit /b 1 )

		start "" %PS_CMD% -Command "Start-Sleep -Seconds 2; $title='Portable Git for Windows 64-bit'; $window=Get-Process | Where-Object { $_.MainWindowTitle -eq $title } | Select-Object -First 1; if ($window -ne $null) { [void][System.Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic'); [Microsoft.VisualBasic.Interaction]::AppActivate($window.Id); Start-Sleep -Seconds 1; Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait('{ENTER}') }"

		echo "設定を変更せずに、そのままインストールしてください。"
		%APP_LIB_DIR%\PortableGit.7z.exe
		if !errorlevel! neq 0 ( pause & popd & exit /b 1 )

		echo del %APP_LIB_DIR%\PortableGit.7z.exe
		del %APP_LIB_DIR%\PortableGit.7z.exe
		if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
	)
)

if exist %PORTABLE_GIT_DIR% (
	echo set "PATH=%PORTABLE_GIT_DIR%;%PATH%"
	set "PATH=%PORTABLE_GIT_DIR%;%PATH%"

	where /Q git
	if !errorlevel! neq 0 (
		echo [Error] git を自動インストールできませんでした。Git for Windows を手動でインストールしてください。
		start https://gitforwindows.org/
		pause & popd & exit /b 1
	)
	cd > NUL

	if exist .git\ (
		echo git pull
		git pull
	) else (
		echo git clone %CLONE_URL% %APP_NAME_TEMP%
		git clone %CLONE_URL% %APP_NAME_TEMP%
	)
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
) else (
	if exist .git\ (
		echo git pull
		git pull
	) else (
		echo git clone %CLONE_URL% %APP_NAME_TEMP%
		git clone %CLONE_URL% %APP_NAME_TEMP%
	)
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)

if exist %APP_NAME_TEMP%\ (
	echo xcopy /SQYh %APP_NAME_TEMP%\ .
	xcopy /SQYh %APP_NAME_TEMP%\ .
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )

	echo rmdir /S /Q %APP_NAME_TEMP%\
	rmdir /S /Q %APP_NAME_TEMP%\
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)
endlocal

call %APP_NAME%\setup\Setup-%APP_NAME%.bat
if %errorlevel% neq 0 ( popd & exit /b 1 )

start "" Run-%APP_NAME%.bat

popd
if not exist %~dp0Install-%APP_NAME%.bat ( exit /b 0 )
del %~dp0Install-%APP_NAME%.bat