@echo off
chcp 65001 > NUL
pushd %~dp0
set CURL_CMD=C:\Windows\System32\curl.exe -k

@REM 7B: 33, 35B: 41, 70B: 65
set GPU_LAYERS=0

@REM 2048, 4096, 8192, 16384, 32768, 65536, 131072
set CONTEXT_SIZE=16384

if not exist Ocuteus-v1-q8_0.gguf (
    start "" https://huggingface.co/Local-Novel-LLM-project/Ocuteus-v1-gguf
    start "" https://huggingface.co/Local-Novel-LLM-project/Ocuteus-v1-gguf/blob/main/Modelfile-Ocuteus-v1

    %CURL_CMD% -LO https://huggingface.co/Local-Novel-LLM-project/Ocuteus-v1-gguf/resolve/main/Ocuteus-v1-q8_0.gguf
)

if not exist Ocuteus-v1-mmproj-f16.gguf (
    %CURL_CMD% -LO https://huggingface.co/Local-Novel-LLM-project/Ocuteus-v1-gguf/resolve/main/Ocuteus-v1-mmproj-f16.gguf
)

koboldcpp.exe --gpulayers %GPU_LAYERS% --usecublas --contextsize %CONTEXT_SIZE% --mmproj Ocuteus-v1-mmproj-f16.gguf --launch Ocuteus-v1-q8_0.gguf
if %errorlevel% neq 0 ( pause & popd & exit /b 1 )
popd
