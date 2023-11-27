import sys
from aip import AipSpeech # 导入api接口
import os

# 获取环境变量值，如果不存在则使用默认值
APP_ID = os.environ.get('APP_ID', 'default_app_id')
API_KEY = os.environ.get('API_KEY', 'default_api_key')
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

response_file = sys.argv[1]  # 获取Shell脚本传递的参数，即文本文件名
audio_file = sys.argv[2]  # 获取Shell脚本传递的参数，即音频文件名

with open(response_file, 'r', encoding='utf-8') as f:
    data = f.read()

# with open(r'/tmp/sidBox/response.txt', 'r', encoding='utf-8') as f:
#     data = f.read()

'''
'per': 4  发声人选择，0为女声,1为男声,3为情感合成-度逍遥,4为情感合成-度丫丫，默认为普通女
'''
result = client.synthesis(
    data,
    'zh',
    1,
    {
        'per': 4,
        'spd': 6,  # 速度
        'vol': 9,  # 音量
        'aue': 6
    })

if not isinstance(result, dict):
    with open(audio_file, 'wb') as f:
        f.write(result)
# print(result)