#!/bin/bash

requirements_command=("curl" "git" "tar" "python")

# check requirements command exists
for  i in "${requirements_command[@]}"
do
    if ! command -v "$i" &> /dev/null; then
        echo "[ERROR] $i  が見つかりません。お使いのパッケージマネージャでインストールしてください。"
        flag_not_found=true
    fi
done

if [ "$flag_not_found" = true ]; then
    exit 1
fi

if ! python -c "import tkinter" &> /dev/null; then
    echo "[ERROR] tkintr が見つかりません。お使いのパッケージマネージャで「python3-tk」をインストールしてください。"
    exit 1
fi

GITHUB="Zuntan03"
APP_NAME="EasyNovelAssistant"
APP_VENV_DIR="venv"
CLONE_URL="https://github.com/"$GITHUB"/EasyNovelAssistant"

if [ ! -d "$APP_VENV_DIR" ]; then
    echo "https://github.com/"$GITHUB"/EasyNovelAssistant"
    echo "https://github.com/LostRuins/koboldcpp"
    echo
    echo "https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF"
    echo "https://huggingface.co/Sdff-Ltba/LightChatAssistant-2x7B-GGUF"
    echo "https://huggingface.co/Aratako/LightChatAssistant-4x7B-GGUF"
    echo "https://huggingface.co/Aratako/SniffyOtter-7B-Novel-Writing-NSFW-GGUF"
    echo "https://huggingface.co/Elizezen/SniffyOtter-7B-GGUF"
    echo "https://huggingface.co/Aratako/Antler-7B-Novel-Writing-GGUF"
    echo "https://huggingface.co/TFMC/Japanese-Starling-ChatV-7B-GGUF"
    echo "https://huggingface.co/andrewcanis/c4ai-command-r-v01-GGUF"
    echo "https://huggingface.co/dranger003/c4ai-command-r-plus-iMat.GGUF"
    echo "https://huggingface.co/pmysl/c4ai-command-r-plus-GGUF"
    echo
    echo "以上の配布元から関連ファイルをダウンロードして利用します。"
    read -p "よろしいですか？ [y/n] " YES_OR_NO
    if [ "$YES_OR_NO" != "y" ]; then
        exit 1
    fi
fi

git clone $CLONE_URL
# check return status
if [ $? -ne 0 ]; then
    echo "[ERROR] git clone に失敗しました。"
    exit 1
fi

cd $APP_NAME

chmod +x $APP_NAME/setup/Setup-$APP_NAME.sh
$APP_NAME/setup/Setup-$APP_NAME.sh

chmod +x ./Run-$APP_NAME.sh
./Run-$APP_NAME.sh

cd -

if [ -f "$(pwd)/Install-$APP_NAME.sh" ]; then
    rm "$(pwd)/Install-$APP_NAME.sh"
fi
