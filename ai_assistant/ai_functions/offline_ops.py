import os
import subprocess as sp
from ai_functions.core_ops import speak
import pyaudio
import wave
import datetime



AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_RATE = 44100
CHUNK_SIZE = 1024


paths = {
    'notepad': r'C:\Windows\notepad.exe',
    'calculator': r'C:\Windows\System32\calc.exe',
    'autoClicker': r'C:\Users\georg\Desktop\AutoClicker.exe'
}




def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    sp.Popen([r'C:\Windows\notepad.exe', file_name])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_autoClicker():
    os.startfile(paths['autoClicker'])

def open_cmd():
    os.system('start cmd')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def rickroll():
    try:
        sp.run(['start', '', r"env\rickroll.mp4"], shell=True)
    except Exception as e:
        print(f"Error: {e}")










