import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
import random

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     # print("Enter the word you want to speak it out by Computer")
#     s = input()
#     speaker.Speak(s)


# def say(text):
#     os.system(f"say {text}")
def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n******************************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[],
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1, 26844627872172)}") as f:
        f.write(text)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred, Sorry from Jarvis"


if __name__ == '__main__':
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print('PyCharm')
    speaker.Speak(" Jarvis A. I")
    print("Listening...")
    query = take_command()
    sites = {"youtube": "https://youtube.com", "google": "https://www.google.com",
             "wikipedia": "https://www.wikipedia.com"}
    for items in sites:
        if f"Open {items}".lower() in query.lower():
            speaker.Speak(f"Opening {items} Sir")
            webbrowser.open(sites[items])
    if "play music".lower() in query:
        music_path = ""
        os.startfile(music_path)
    if "time".lower() in query:
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.Speak(f"The time is {strfTime}")
    if "open whatsapp".lower() in query.lower():
        os.system(f"")
    if "using artificial intelligence".lower() in query.lower():
        ai(prompt=query)
