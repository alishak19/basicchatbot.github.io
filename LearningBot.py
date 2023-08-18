import transformers

import speech_recognition as sre
from gtts import gTTS

import os
import time

import numpy as np
import datetime

# building the AI learning bot class

class LearningBot(): 
  def_init_(self, name): 
    print("waking up", name, "")
    self.name = name
  def speech_to_text(self):
    recognizer = sre.Recognizer()
    with sre.Microphone() as micdrop:
      print("listening to you...")
      audio = recognizer.listen(micdrop)
      self.text="ERROR"
    try: 
      self.text = recognizer.recognize_google(audio)
      print("who me?? ", self.text)
    except:
      print("who me?? ERROR")
  @staticmethod
  def text_to_speech(text):
    print("Dev --> ", text)
    speaker = gTTS(text=text, lang="en", slow=False)
    speaker.save("res.mp3")
    statbuf = os.stat("res.mp3")
    mbytes = statbuf.st_size / 1024
    duration = mbytes / 200
    os.system('afplay res.mp3')
    time.sleep(int(50*duration))
    os.remove("res.mp3")
  def wake_up(self, text)
    return True if self.name in text.lower() else False
  @staticmethod
  def action_time(): 
    return datetime.datetime.now().time().strftime('%H:%M')
#turn the ai into a runner/track star
if __name__ == "__main__":
  ai = LearningBot(name="dev")
  nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
  os.environ["TOKENIZERS_PARALLELISM"] = "true"
  ex=True
  while ex:
    ai.speech_to_text()
    if ai.wake_up(ai.text) is True:
      res = "howdy! i'm dev :D"
    elif "time" in ai.text:
      res = ai.action_time()
    elif any (i in ai.text for i in ["thank","thanks"]):
      res = np.random.choice(["you're so welcome it's not even funny","slay", "ur welc"])
    elif any (i in ai.text for i in ["taylor","swift"]):
      res = np.random.choice(["your midas touch on the chevy door, november flush and your flannel cure","this dorm was once a madhouse, i made a joke well it's made for me","how evergreen your group of friends, don't think we'll say that word again","and soon they'll have the nerve to deck the halls that we once walked through","one for the money, two for the show, i never was ready so i watched you go","sometimes you just don't know the answer till someone's on their knees and asks you","she would've made such a lovely bride, what a shame she's stuck in her head, they said","but you'll find the real thing instead, and she'll patch up the tapestry that I shred"])
    elif any(i in ai.text for i in ["exit","close"]):
      res = np.random.choice(["slayed","have a great day not just a good day","fine leave me alone then"])
      ex=False
    else: 
      if ai.text=="ERROR":
        res="i don't have a fitting taylor swift lyric for this moment. given that that's basically impossible, please try again"
      else:
        chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("bot >> ")+6:].strip()
    ai.text_to_speech(res)
  print("night Dev")
      

