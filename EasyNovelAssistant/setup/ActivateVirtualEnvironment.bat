@echo off
chcp 65001 > NUL
set PS_CMD=PowerShell -Version 5.1 -ExecutionPolicy Bypass
set CURL_CMD=C:\Windows\System32\curl.exe --ssl-no-revoke
set PYTHON_CMD=python

set PYTHON_DIR=%~dp0lib\python
set LOCAL_PYTHON_CMD=%PYTHON_DIR%\python.exe

for /f "tokens=*" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VERSION_VAR=%%i
if not "%PYTHON_VERSION_VAR:~7,4%"=="3.10" (
	set PYTHON_CMD=%LOCAL_PYTHON_CMD%
	if not exist %PYTHON_DIR%\ (
		echo https://www.python.org/
		echo https://github.com/pypa/get-pip
		mkdir %PYTHON_DIR%

		echo %CURL_CMD% -o %~dp0lib\python.zip https://www.python.org/ftp/python/3.10.6/python-3.10.6-embed-amd64.zip
		%CURL_CMD% -o %~dp0lib\python.zip https://www.python.org/ftp/python/3.10.6/python-3.10.6-embed-amd64.zip
		if %errorlevel% neq 0 ( pause & exit /b 1 )

		echo %PS_CMD% Expand-Archive -Path %~dp0lib\python.zip -DestinationPath %PYTHON_DIR%
		%PS_CMD% Expand-Archive -Path %~dp0lib\python.zip -DestinationPath %PYTHON_DIR%
		if %errorlevel% neq 0 ( pause & exit /b 1 )

		echo del %~dp0lib\python.zip
		del %~dp0lib\python.zip
		if %errorlevel% neq 0 ( pause & exit /b 1 )

		echo %PS_CMD% "try { &{(Get-Content '%PYTHON_DIR%/python310._pth') -creplace '#import site', 'import site' | Set-Content '%PYTHON_DIR%/python310._pth' } } catch { exit 1 }"
		%PS_CMD% "try { &{(Get-Content '%PYTHON_DIR%/python310._pth') -creplace '#import site', 'import site' | Set-Content '%PYTHON_DIR%/python310._pth' } } catch { exit 1 }"
		if %errorlevel% neq 0 ( pause & exit /b 1 )

		echo %CURL_CMD% -o %PYTHON_DIR%\get-pip.py https://bootstrap.pypa.io/get-pip.py
		%CURL_CMD% -o %PYTHON_DIR%\get-pip.py https://bootstrap.pypa.io/get-pip.py
		@REM プロキシ環境用コマンド。ただし動作未確認、かつ Python をインストールしたほうが楽そう。
		@REM %CURL_CMD% -o %PYTHON_DIR%\get-pip.py https://bootstrap.pypa.io/get-pip.py --proxy="PROXY_SERVER:PROXY_PORT"
		if %errorlevel% neq 0 (
			echo "[Error] プロキシ環境によりインストールに失敗した可能性があります。Python 3.10.6 を手動インストールしてパスを通してください。"
			start https://www.python.org/downloads/release/python-3106/
			pause & exit /b 1
		)

		echo %LOCAL_PYTHON_CMD% %PYTHON_DIR%\get-pip.py --no-warn-script-location
		%LOCAL_PYTHON_CMD% %PYTHON_DIR%\get-pip.py --no-warn-script-location
		if %errorlevel% neq 0 ( pause & exit /b 1 )

		echo %LOCAL_PYTHON_CMD% -m pip install virtualenv --no-warn-script-location
		%LOCAL_PYTHON_CMD% -m pip install virtualenv --no-warn-script-location
		if %errorlevel% neq 0 ( pause & exit /b 1 )
	)
)

for /f "tokens=*" %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VERSION_VAR=%%i
if not "%PYTHON_VERSION_VAR:~7,4%"=="3.10" (
	echo %PYTHON_VERSION_VAR%
	echo "[Error] 何らかの理由で Python をインストールできませんでした。Python 3.10.6 を手動インストールしてパスを通してください。"
	start https://www.python.org/downloads/release/python-3106/
	pause & exit /b 1
)

if not "%~1"=="" (
	set VIRTUAL_ENV_DIR=%~1
) else (
	set VIRTUAL_ENV_DIR=venv
)

if not exist %VIRTUAL_ENV_DIR%\ (
	echo %PYTHON_CMD% -m venv %VIRTUAL_ENV_DIR%
	%PYTHON_CMD% -m venv %VIRTUAL_ENV_DIR%

	if not exist %VIRTUAL_ENV_DIR%\ (
		echo %PYTHON_CMD% -m pip install virtualenv --no-warn-script-location
		%PYTHON_CMD% -m pip install virtualenv --no-warn-script-location

		echo %PYTHON_CMD% -m virtualenv --copies %VIRTUAL_ENV_DIR%
		%PYTHON_CMD% -m virtualenv --copies %VIRTUAL_ENV_DIR%
	)

	if not exist %VIRTUAL_ENV_DIR%\ (
		echo "[ERROR] Python 仮想環境を作成できませんでした。Python 3.10.6 を手動でパスを通してインストールしてください。"
		pause & exit /b 1
	)
)

call %VIRTUAL_ENV_DIR%\Scripts\activate.bat
if %errorlevel% neq 0 ( pause & exit /b 1 )
