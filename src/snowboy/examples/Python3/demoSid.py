import os
import snowboydecoder
import sys
import signal

# 获取当前脚本文件的路径
script_dir = os.path.dirname(os.path.realpath(__file__))
interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def callback_function():
    # Play the audio file
    print('paplay wozai.wav')
    # 构建相对路径
    relative_path = "../../../../audio/wozai5s.wav"
    absolute_path = os.path.normpath(os.path.join(script_dir, relative_path))
    # os.system('paplay ../../../../audio/wozai5s.wav --no-remap')
    # 执行shell脚本
    os.system(f'paplay {absolute_path} --no-remap')

    # Check if the script is running
    if os.system('pgrep -f hiSid.sh') == 0:
        # If it is running, kill the process
        os.system('pkill -f hiSid.sh')
    # Run the script
    # os.system('~/whisper/hiSid.sh')
    # 构建相对路径
    relative_path = "../../../../src/hiSid.sh"
    absolute_path = os.path.normpath(os.path.join(script_dir, relative_path))
    os.system(f'{absolute_path}')

    # Exit the script after callback
    # sys.exit(0)


if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=callback_function,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

