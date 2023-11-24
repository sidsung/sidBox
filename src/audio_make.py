from aip import AipSpeech	# 导入api接口

""" 你自己的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

data = '我在呢，请在滴声后五秒内输入语音'

'''
'per': 4  发声人选择，0为女声,1为男声,3为情感合成-度逍遥,4为情感合成-度丫丫，默认为普通女
'''
result = client.synthesis(data, 'zh', 1, {
    'per': 4,
    'spd': 5,    # 速度
    'vol': 10,   # 音量
    'aue': 6
})
if not isinstance(result, dict):
    with open('test.wav', 'wb') as f:
        f.write(result)

