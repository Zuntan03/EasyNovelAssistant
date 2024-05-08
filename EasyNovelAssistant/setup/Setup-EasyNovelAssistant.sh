#!/bin/bash

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

if [ ! -e "koboldcpp-linux-x64-cuda1150" ]; then
    curl -LO https://github.com/LostRuins/koboldcpp/releases/latest/download/koboldcpp-linux-x64-cuda1150
    chmod +x koboldcpp-linux-x64-cuda1150
fi

if [ ! -e "Vecteus-v1-IQ4_XS.gguf" ]; then
    curl -LO https://huggingface.co/mmnga/Vecteus-v1-gguf/resolve/main/Vecteus-v1-IQ4_XS.gguf
fi

cd -
