import os
import subprocess as sp
from ai_functions.core_ops import speak
import pyaudio
import wave
import sys
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
        # Get the absolute path of the video file
        video_path = r"C:\Users\georg\Downloads\JARVIS\env\rickroll.mp4"
        
        # Open the video file with the default media player
        sp.run(['start', '', video_path], shell=True)
    except Exception as e:
        print(f"Error: {e}")












def record_audio_to_file(file_name):
    audio = pyaudio.PyAudio()

    try:
        stream = audio.open(format=AUDIO_FORMAT,
                            channels=1,
                            rate=SAMPLE_RATE,
                            input=True,
                            frames_per_buffer=CHUNK_SIZE)

        speak("Press 'Enter' to start recording...")
        input()  # Wait for the user to start recording

        frames = []
        recording = True
        while recording:
            data = stream.read(CHUNK_SIZE)
            frames.append(data)

            # Check if the user pressed 'Enter' to stop recording
            if input("Press 'Enter' to stop recording...\n") == "":
                recording = False

        print("Recording finished!")

        # Write the recorded frames directly to the file
        with wave.open(file_name, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(audio.get_sample_size(AUDIO_FORMAT))
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(b''.join(frames))

    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()