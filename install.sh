#!/bin/bash

# ===hot word===
# 编译snowboy动态库
cd ./src/snowboy/swig/Python3
make clean
make -j8
cd -
# 安装python3.9虚拟环境
mkdir _install
cd _install
python3.9 -m venv snowboy_venv
source snowboy_venv/bin/activate
pip install pyaudio
# deactivate

# ===baidu asr===
pip install baidu-aip
pip install playsound
pip install chardet

# ===shell gpt===
python3 -m venv chatgpt_cli
source chatgpt_cli/bin/activate
pip install shell-gpt

# ===baidu tts===
pip install baidu-aip
pip install playsound
pip install chardet

deactivate
