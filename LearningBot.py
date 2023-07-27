import transformers

import speech_recognition as sre
from gtts import gTTS

import os
import time

import numpy as np
import datetime

# creating the AI model bot

class LearningBot(): 
  def_init_(self, name): 
    print("Starting up", name, "")
    self.name = name
  def speech_to_text(self):
    recognizer = sre.Recognizer()
    with sre.Microphone() as micdrop:
      print("Listening to you...")
      audio = recognizer.listen(micdrop)
      self.text="ERROR"
    try: 
      self.text = recognizer.recognize_google(audio)
      print("who me?? ", self.text)
    except:
      print("who me?? ERROR")

