@echo off
chcp 65001 > NUL
set CURL_CMD=C:\Windows\System32\curl.exe -k

if not exist %~dp0sample\ ( mkdir %~dp0sample )
pushd %~dp0sample

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/special.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/special.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/template.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/template.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/nsfw.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/nsfw.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/speech.json
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/speech.json
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

popd
if not exist %~dp0sample\GoalSeek\ ( mkdir %~dp0sample\GoalSeek )
pushd %~dp0sample\GoalSeek

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/00-企画.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/00-企画.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/01-執筆.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/01-執筆.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/10-序章.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/10-序章.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/20-第一章.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/20-第一章.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/30-第二章.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/30-第二章.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/40-第三章.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/40-第三章.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

echo %CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/50-終章.txt
%CURL_CMD% -sLO https://yyy.wpx.jp/EasyNovelAssistant/sample/GoalSeek/50-終章.txt
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )

popd
pushd %~dp0
call EasyNovelAssistant\setup\ActivateVirtualEnvironment.bat
if %errorlevel% neq 0 ( popd & exit /b 1 )

python EasyNovelAssistant\src\easy_novel_assistant.py
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )
popd
