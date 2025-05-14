#pip install -U google-generativeai
#pip install pyttsx3
#pip install SpeechRecognition
#pip install datetime
#pip install wikipedia
#pip install pywahtkit
#pip install pyyaml==5.4.1
#pip install pipwin
#pip install pyaudio

import google.generativeai as genai
import os
import pygame
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import vertexai
import time
import winsound
from vertexai.preview.generative_models import GenerativeModel,ChatSession
frequency = 300  # Set Frequency To 2500 Hertz
duration = 600  # Set Duration To 1000 ms == 1 second


time.clock = time.time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
nome = "Jarvis"
primeiro = 1


vertexai.init(project="vxgva1", location="us-central1")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

os.environ["GOOGLE_API_KEY"] = "AIzaSyDxAbYdnjk3lmyTrcWeQ4QZoBnhvTusKzA"


from openai import OpenAI

client = OpenAI(api_key="AIzaSyDxAbYdnjk3lmyTrcWeQ4QZoBnhvTusKzA")
genai.configure(api_key="AIzaSyDxAbYdnjk3lmyTrcWeQ4QZoBnhvTusKzA")

pygame.mixer.init()

#gemini
def chatfun(chat: ChatSession, prompt: str) -> str:
    response = chat.send_message(prompt)
    return response.text

#text to speech
def speak(audio):

    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 240)
    engine.setProperty("volume", 1.)
    engine.say(audio)
    # print(audio)
    engine.runAndWait()



#Convert voice into text
def takecommand():
    r = sr.Recognizer()
    wait = True
    with sr.Microphone() as source:
        winsound.Beep(frequency, duration)
        print("listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source,timeout=6,phrase_time_limit=6)
            if wait is False:
                return "none"
        except Exception as e:
            return "none"
    try:
        print("Recognizing...")
        #query = r.recognize_google(audio, language='en-in')
        query = r.recognize_google(audio, language='pt-BR')
        print(f"user said: {query}")
        wait = False
    except Exception as e:
        #speak("Say that again please...")
        #speak("Hey Julio, não compreendi. pode repetir? ")
        #speak("")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour<=12:
        #speak("good morning")
        speak("Bom Dia")
    elif hour >= 12 and hour <= 18:
        #speak("good afternoon")
        speak("Boa Tarde")
    else:
        #speak("good evening")
        speak("Boa Noite")
    #speak("I am jarvis sir. , please tell me how can i help you")
    speak(f"Sou {nome}, a seu comando. Como posso ser útil? ")


if __name__ == "__main__":
    if primeiro == 1:
        wish()
        primeiro = 0


    while True:
        query = takecommand().lower()
        print(query)



        #query = "procurar por Homem de Ferro"
        if (("abrir bloco de notas") in query) and (("jarvis") in query):
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif (("procurar por" or "me diz sobre" or "me informa sobre" or "informações sobre") in query) and (("jarvis") in query):
            query = query.replace("jarvis", "")
            procurar = query.replace("procurar por","")
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar,2)
            speak(resultado)
            print(resultado)

        elif (("tocar" or "dar play em" or "toca" or "manda um som do" or "toca uma musica do") in query) and (("jarvis") in query) :
            speak("È pra já. ")
            query = query.replace("jarvis", "")
            musica = query.replace("tocar","")
            musica = musica.replace("dar play em","")
            musica.replace("Jarvis", "")
            pywhatkit.playonyt(musica)
            break
        elif (("não" or "nao") in query) and (len(query) < 15):
            speak("Ok, precisando estarei por aqui!")
            break

        else:
            try:

                if len(query) > 4:
                    #if ("jarvis") in query:
                    # resp = api.send_message(query)
                        query = query.replace("jarvis", "")
                        #resp = chatGPT(query)
                        resp = chatfun(chat, query)
                        print(resp)
                        resp = resp.replace("*","")
                        print (len(resp))
                        if len(resp) < 15:
                            speak(resp)


                        #speak("Algo mais em que eu possa te ajudar? ")
                   # else:
                        print("ok")

                else:
                    print("Hey Julio, não compreendi. pode repetir? ")

            except(KeyboardInterrupt, EOFError, SystemExit):
                break






