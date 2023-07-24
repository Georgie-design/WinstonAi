from variables import USERNAME, BOTNAME, engine_rate, engine_volume, engine_gender, engine_name
import speech_recognition as sr
from datetime import datetime
import pyttsx3
import pygame

engine = pyttsx3.init(engine_name)

def play_audio(audio_file_path):
    pygame.init()
    sound = pygame.mixer.Sound(audio_file_path)
    sound.play()

    clock = pygame.time.Clock()
    while pygame.mixer.get_busy():
        clock.tick(30)

    pygame.quit()

def configure_engine():
    engine = pyttsx3.init(engine_name)
    engine.setProperty('rate', engine_rate)
    engine.setProperty('volume', engine_volume)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[engine_gender].id)

def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        play_audio(r'ai_assistant\Voice\good_morning_master.mp3')
    elif (hour >= 12) and (hour < 16):
        play_audio(r'ai_assistant\Voice\good afternoon master.mp3')
    elif (hour >= 16) and (hour < 23):
        play_audio(r'ai_assistant\Voice\good evening master.mp3')
    play_audio(r'ai_assistant\Voice\assistance.mp3')

def speak(text):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en').lower()
        print(f'{BOTNAME} heard: '+ query)

    except Exception:
        play_audio(r'ai_assistant\Voice\repeat that.mp3')
        query = 'None'
    return query

def goodbye():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        play_audio(r'ai_assistant\Voice\good night.mp3')
    else:
        play_audio(r'ai_assistant\Voice\have a good day master.mp3')
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def play_sound(audio_file_path):
    pygame.init()
    sound = pygame.mixer.Sound(audio_file_path)
    sound.play()

    clock = pygame.time.Clock()
    while pygame.mixer.get_busy():
        clock.tick(30)

    pygame.quit()


