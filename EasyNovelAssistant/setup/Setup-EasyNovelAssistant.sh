#!/usr/bin/bash

# create and activate venv
if [ ! -d "venv" ]; then
    python -m venv venv
fi
source venv/bin/activate

# install pip packages
pip install -r ./EasyNovelAssistant/setup/res/requirements.txt

# download kobold cpp
mkdir -p KoboldCpp
cd KoboldCpp

if [ ! -e "koboldcpp-linux-x64" ]; then
    curl -LO https://github.com/LostRuins/koboldcpp/releases/download/v1.63/koboldcpp-linux-x64
    chmod +x koboldcpp-linux-x64
fi

if [ ! -e "LightChatAssistant-TypeB-2x7B_iq4xs_imatrix.gguf" ]; then
    curl -LO https://huggingface.co/Sdff-Ltba/LightChatAssistant-TypeB-2x7B-GGUF/resolve/main/LightChatAssistant-TypeB-2x7B_iq4xs_imatrix.gguf
fi

cd -
