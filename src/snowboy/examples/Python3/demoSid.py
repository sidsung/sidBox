import os
import snowboydecoder
import sys
import signal

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
    os.system('paplay /home/sidsung/whisper/baidu_tts/audio_files/wozai5s.wav --no-remap')

    # Check if the script is running
    if os.system('pgrep -f hiSid.sh') == 0:
        # If it is running, kill the process
        os.system('pkill -f hiSid.sh')
    # Run the script
    os.system('~/whisper/hiSid.sh')

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

