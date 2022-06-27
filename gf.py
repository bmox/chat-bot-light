blender_bot_app_url="https://40077.gradio.app/"
app_url="https://59322.gradio.app/"
import json
import requests

import base64

file_name="temp.wav"
def natural_SpeakText(mytext):
    r = requests.post(url=app_url+"api/predict/",
    json={"data":
    [mytext]})
    audio_data=r.json()
    raw_data=audio_data["data"][0].replace("data:audio/wav;base64,","")
    wav_file = open(file_name, "wb")
    decode_string = base64.b64decode(raw_data)
    wav_file.write(decode_string)
    music = pyglet.media.load(file_name, streaming=False)
    music.play()
    sleep(music.duration)
    
    
from rich.console import Console
console = Console()
db={}
db["output_language"] = "en"
db["input_language"] = "en"
def input_language_set(in_lang):
  if in_lang == "input language english":
      db["input_language"] = "en"
      text="Now you can talk with me in  english"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language hindi":
      db["input_language"] = "hi"
      text="Now you can talk with me in  hindi"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language bengali":
      db["input_language"] = "bn"
      text="Now you can talk with me in  bengali"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language korean":
      db["input_language"] = "ko"
      text="Now you can talk with me in  korean"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language chinese":
      db["input_language"] = "zh-cn"
      text="Now you can talk with me in  chinese"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language japanese":
      db["input_language"] = "ja"
      text="Now you can talk with me in  japanese"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif in_lang == "input language spanish":
      db["input_language"] = "es"
      text="Now you can talk with me in  spanish"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)

def output_language_set(out_lang):
  if out_lang == "output language english":
      db["output_language"] = "en"
      text="From now i will talk with you in english."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language hindi":
      db["output_language"] = "hi"
      text="From now i will talk with you in hindi."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language bengali":
      db["output_language"] = "bn"
      text="Now you can talk with me in  bengali"
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language korean":
      db["output_language"] = "ko"
      text="From now i will talk with you in korean."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language chinese":
      db["output_language"] = "zh-cn"
      text="From now i will talk with you in chinese."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language japanese":
      db["output_language"] = "ja"
      text="From now i will talk with you in japanese."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
  elif out_lang == "output language spanish":
      db["output_language"] = "es"
      text="From now i will talk with you in spanish."
      text=trans_msg(text)
      console.print(f"[bold green]BOT:[/bold green] {text}\n",style="yellow")
      SpeakText(text)
      

from googletrans import Translator
translator = Translator()

def trans_bot(mytext):
    result = translator.translate(mytext,dest="en")
    return str(result.text)  

def trans_msg(mytext):
    result = translator.translate(mytext,dest=db["output_language"])
    return str(result.text) 



def blender_bot(msg):
    r = requests.post(url=blender_bot_app_url+"api/predict/",
    json={"data":
    [msg]})
    json_reply=r.json()
    english_chat=json_reply['data'][0]
    if db["output_language"] != "en":
        english_chat=trans_msg(english_chat)
    console.print(f"[bold green]BOT:[/bold green] {english_chat}\n",style="yellow")
    SpeakText(english_chat)
    return english_chat

def preprocess(msg):
    input_language_set(msg)
    output_language_set(msg)
    if db["input_language"] != "en":
        msg=trans_bot(msg)
    if "output language"  in msg or "input language" in msg:
        pass
    else:
        blender_bot(msg)
   
from time import sleep
import pyglet
import os
from gtts import gTTS

def SpeakText(mytext):
    google_tts(mytext)
           
# def SpeakText(mytext):
#     if db["output_language"]=="en":
#         try:
#             natural_SpeakText(mytext)
#         except:
#             google_tts(mytext)
#     else:
#         google_tts(mytext)
        
    
def google_tts(mytext):
    tts = gTTS(text=mytext,tld="ca", lang=db["output_language"])
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)      
  

import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
print("Let's speak!!")

while True:
    
    try:
        with sr.Microphone( sample_rate = 48000,chunk_size = 2048) as source:
            r.adjust_for_ambient_noise(source)
            console.print(f"[bold blue]Listening[/bold blue] ")
            audio = r.listen(source)
            text = r.recognize_google(audio,language=db["input_language"])
            MyText = text.lower()
            console.print(f"[bold blue]YOU:[/bold blue] {MyText}",style="yellow")
            preprocess(MyText)
    except Exception as e:
        print(e)
