import pyttsx3 as p
import speech_recognition as sr
from selenium_new import *
from yt_autor import *
import randfacts
from jokes import *
import datetime
import time
import threading

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
speak("Hello Mam, I am your Voice Assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    if "what about you" in text.lower():
        speak("I am having a good day Mam")

video_thread = None

while True:
    speak("What can I do for you?")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)

    if "information" in text2.lower():
        speak("You need information related to which topic?")
        with sr.Microphone() as source:
            r.energy_threshold = 1000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening")
            audio = r.listen(source)
            infor = r.recognize_google(audio)
        speak("Searching {} in Wikipedia".format(infor))
        assist = Inflow()
        assist.get_info(infor)

    elif "play " in text2.lower() or "video" in text2.lower():
        speak("You want me to play which video?")
        with sr.Microphone() as source:
            r.energy_threshold = 1000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
        print("Playing {} on YouTube".format(vid))

        def play_video():
            assist = Music()
            assist.play(vid)

        video_thread = threading.Thread(target=play_video)
        video_thread.start()

        while video_thread.is_alive():
            time.sleep(1)  # Wait for the video to finish

        video_thread.join()
        speak("What can I do for you?")

    elif "fact" in text2.lower() or "facts" in text2.lower():
        speak("Sure, Mam")
        x = randfacts.getFact()
        print(x)
        speak("Did you know that, " + x)

    elif "joke" in text2.lower() or "jokes" in text2.lower():
        speak("Sure, get ready for some chuckles")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])

    elif "date" in text2.lower():
        current_date = datetime.date.today()
        speak(str(current_date))

    elif "thank you" in text2.lower() or "bye" in text2.lower():
        speak("Have a nice day")
        break

    else:
     break

