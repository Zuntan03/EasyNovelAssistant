@echo off
chcp 65001 > NUL
set CURL_CMD=C:\Windows\System32\curl.exe --ssl-no-revoke

if not exist %~dp0sample\ ( mkdir %~dp0sample )
pushd %~dp0sample

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/template.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/template.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

setlocal enabledelayedexpansion
if exist nsfw.json (
	echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/nsfw.json
	%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/nsfw.json
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)
if exist speech.json (
	echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/speech.json
	%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/speech.json
	if !errorlevel! neq 0 ( pause & popd & exit /b 1 )
)
endlocal
popd

pushd %~dp0
call EasyNovelAssistant\setup\ActivateVirtualEnvironment.bat
if %errorlevel% neq 0 ( popd & exit /b 1 )

python EasyNovelAssistant\src\easy_novel_assistant.py
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )
popd
