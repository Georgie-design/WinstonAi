import openai
import pyttsx3
import json 
from variables import OpenAi_API_key as key


from variables import engine_name, engine_gender
from .core_ops import speak

def write_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            file.write("\n")  # Add a new line after writing the content, if desired
        print("Content has been successfully written to the file.")
    except IOError:
        print("An error occurred while writing to the file.")

def chat(chat_query):
    openai.api_key = key
    conversation = [
        {'role': 'system', 'content': "You are a helpful British AI Voice Assistant"},
        {'role': 'user', 'content': chat_query}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    reply_content = completion.choices[0].message.content
    engine = pyttsx3.init(engine_name)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    speak(reply_content)
    print(reply_content)
    engine.setProperty('voice', voices[0].id)

    conversation.append({'role': 'assistant', 'content': reply_content})

    # Convert the conversation list to a JSON string before writing to the file
    conversation_json = json.dumps(conversation, indent=2)
    write_to_file('conversation.txt', conversation_json)

    speak('Exiting ChatGPT')