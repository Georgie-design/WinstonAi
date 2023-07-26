import requests
import pywhatkit as kit









def find_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def play_on_youtube(video):
    kit.playonyt(video)

