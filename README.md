# sidBox
sidBox smart speaker

|hot word|asr|chatGPT|TTS|
|-|-|-|-|
|snowboy|baidu_asr|shellgpt|baidu_tts|

# Device info
- orangePi 5 plus
- 第三方Ubuntu22系统

# How to use
## install
```shell
./install.sh
```
## api keys
- 需要在环境变量中设置`open ai`和`百度`的`api key`等信息
## run
```shell
./start
Listening... Press Ctrl+C to exit
```
- 启动后对着麦克风说 `"hi sid"` 唤醒设备
- 唤醒设备后在嘀声后5秒内输入语音

# Details
## snowboy
### 编译
- 修改Python3目录下的Makefile，使其调用`aarch64`目录下的动态库

### 制作模型
[Snowboy Personal Wake Word (hahack.com)](https://snowboy.hahack.com/)

### 测试运行
- 运行之前先检查一下麦克风录音是否正常
```shell
# 录制音频文件
rec test.wav

# 播放音频文件
play test.wav
```

- 运行
```shell
python3 demo.py snowboy.pmdl
```
- 如果脚本报错可能需要升级pyaudio版本（由于python3.10的某个重大更新）
- 升级pyaudio为0.2.12及以上
```shell
pip install --upgrade pyaudio
```
- 或者尝试低版本python
```shell
sudo apt install python3.9

python3.9 -m venv snowboy_venv
python3 -m pip install --upgrade pip setuptools wheel

```

## baidu asr and tts
### install
```shell
pip install baidu-aip	# 百度的接口
pip install playsound
pip install chardet
```
### api key
- 需要在环境变量中设置自己baidu api key等信息
```shell
vim ~/.bashrc
export APP_ID=''
export API_KEY=''
export SECRET_KEY=''
source ~/.bashrc
```

# shell gpt
### install
```shell
python3 -m venv chatgpt_cli
source chatgpt_cli/bin/activate
pip install shell-gpt
```
### api key
- 需要在环境变量中设置自己openai api key
```shell
vim ~/.bashrc
export OPENAI_API_KEY=
source ~/.bashrc
```
### 测试
```shell
source chatgpt_cli/bin/activate
sgpt "hi"
Hello! How can I assist you today?
```