#!/bin/bash

mkdir -p sample
cd sample
curl  -LO https://yyy.wpx.jp/EasyNovelAssistant/sample/template.json

if [ $? -ne 0 ]; then
    exit 1
fi

curl  -LO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
if [ $? -ne 0 ]; then
    exit 1
fi

if [ -e "nsfw.json" ]; then
    curl  -LO https://yyy.wpx.jp/EasyNovelAssistant/sample/sample.json
fi

cd -

source ./venv/bin/activate
python ./EasyNovelAssistant/src/easy_novel_assistant.py
