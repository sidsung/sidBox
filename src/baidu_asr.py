import wave
import pyaudio
import json
from aip import AipSpeech
import os

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
CHUNK = 1024
FORMAT = pyaudio.paInt16  # 16位深
CHANNELS = 1  #1是单声道，2是双声道。
RATE = 16000  # 采样率，调用API一般为8000或16000
RECORD_SECONDS = 5  # 录制时间

# 获取当前脚本文件的路径
script_dir = os.path.dirname(os.path.realpath(__file__))


def save_wave_file(pa, filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(data))
    wf.close()


def get_audio(filepath):
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)
    print("*" * 10, "开始录音：请在5秒内输入语音")
    relative_path = "./snowboy/examples/Python3/resources/ding.wav"
    absolute_path = os.path.normpath(os.path.join(script_dir, relative_path))
    # 执行shell脚本
    os.system(f'paplay {absolute_path} --no-remap')

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)  # 读取chunk个字节 保存到data中
        frames.append(data)  # 向列表frames中添加数据data
    print("*" * 10, "录音结束\n")
    stream.stop_stream()
    stream.close()  # 停止数据流
    pa.terminate()  # 关闭PyAudio

    #写入录音文件
    save_wave_file(pa, filepath, frames)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    filepath = '/tmp/sidBox/test.wav'
    get_audio(filepath)
    print('over!!!')
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    ret = client.asr(get_file_content('/tmp/sidBox/test.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    print('get ret from baidu asr:')
    print(ret)

    # 将字典对象转换为JSON格式
    Result = json.dumps(ret)
    Result_dict = json.loads(Result)
    if 'result' in Result_dict:
        with open('/tmp/sidBox/output.wav.txt', 'w') as f:
            f.write(Result_dict['result'][0])
        print('保存如下语言识别结果到/tmp/sidBox/output.wav.txt:')
        print(Result_dict['result'][0])
    else:
        print(Result)
