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

python3.9 -m venv sidBox_venv
source sidBox_venv/bin/activate
# ===snwoboy===
pip install pyaudio

# ===baidu===
pip install baidu-aip
pip install playsound
pip install chardet

# ===shell gpt===
pip install shell-gpt
