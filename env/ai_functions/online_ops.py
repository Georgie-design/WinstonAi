import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
import config
from variables import EMAIL, PASSWORD
import yagmail
import openai









def find_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def play_on_youtube(video):
    kit.playonyt(video)

def send_email(receiver_address, subject, message):
    try:
        # Initialize yagmail SMTP connection using your email and password/App Password
        yag = yagmail.SMTP(EMAIL, PASSWORD)

        # Send the email
        yag.send(
            to=receiver_address,
            subject=subject,
            contents=message
        )

        return True
    except Exception as e:
        print(e)
        return False