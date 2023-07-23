from datetime import datetime
from ai_functions.offline_ops import note, open_calculator, open_autoClicker, open_cmd, open_camera, rickroll
from ai_functions.core_ops import speak, take_user_input
from variables import USERNAME, BOTNAME, engine_rate, engine_name
from ai_functions.online_ops import find_ip, play_on_youtube
import pyttsx3
from ai_functions.core_ops import play_audio
import sys
from ai_functions.chatGPT import chat
engine = pyttsx3.init(engine_name)


def analyze_query(query):

    if 'exit' in query or 'stop' in query:
        sys.exit()


    play_audio(r'env\Voice\service.mp3')

    if 'notepad' in query or 'note' in query:
        play_audio(r'env\Voice\note content.mp3')
        text = take_user_input()
        note(text)
        play_audio(r'env\Voice\opening notepad.mp3')

    if 'math' in query or 'calculator' in query:
        open_calculator()
        play_audio(r'env\Voice\opening calculator.mp3')

    if 'auto clicker' in query:
        open_autoClicker()
        play_audio(r'env\Voice\launching autoclicker.mp3')

    if 'rickroll' in query or 'rick roll' in query:
        rickroll()
        play_audio(r'env\Voice\rickroll.mp3')
        

    if 'command prompt' in query or 'terminal' in query:
        open_cmd()
        play_audio(r'env\Voice\hacker shades.mp3')
        


    if 'camera' in query or 'smile' in query or 'take photo' in query or 'take a photo' in query:
        open_camera()
        play_audio(r'env\Voice\say chesse.mp3')

    if 'ip' in query:
        play_audio(r'env\Voice\ip address.mp3')
        engine.setProperty('rate', 5)
        speak(find_ip())
        engine.setProperty('rate', engine_rate)

    if 'play' in query and 'video' in query:
        play_audio(r'env\Voice\which video.mp3')
        video_name = take_user_input()
        play_audio(r'env\Voice\now playing.mp3')
        speak(video_name)
        play_on_youtube(video_name)
        

   
    

    if 'chat' in query:
        speak('Activate ChatGPT? Yes or No.')
        answer = take_user_input()
        if 'no' in answer:
            exit()
        else:
            speak('Activated ChatGPT, What do you want to ask it?')
            answer = take_user_input()
            chat(answer)



        

