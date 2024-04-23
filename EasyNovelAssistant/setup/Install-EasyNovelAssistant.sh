#!/bin/sh

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

APP_NAME="EasyNovelAssistant"
APP_VENV_DIR="venv"
CLONE_URL="https://github.com/Zuntan03/EasyNovelAssistant"

if [ -d "$APP_VENV_DIR" ]; then
    echo "https://github.com/Zuntan03/EasyNovelAssistant"
    echo "https://github.com/LostRuins/koboldcpp"
    echo
    echo "https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF"
    echo "https://huggingface.co/Sdff-Ltba/LightChatAssistant-2x7B-GGUF"
    echo "https://huggingface.co/Aratako/LightChatAssistant-4x7B-GGUF"
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

$APP_NAME/setup/Setup-$APP_NAME.sh

push $APP_NAME
./Run-$APP_NAME.sh

popd

if [ -f "$(pwd)/Install-$APP_NAME.sh" ]; then
    rm "$(pwd)/Install-$APP_NAME.sh"
fi
