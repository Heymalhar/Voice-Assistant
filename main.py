import pyttsx3 as p # Module for text to speech
import speech_recognition as sr # Module for speech to text
from selenium_web import *
from youtube import *
from news import *
import randfacts
from joke import *
from weather import *
import datetime
from translation import *

engine = p.init()

# Rate of speaking
rate = engine.getProperty('rate')
engine.setProperty('rate', 300)
# print(rate)

# Change the voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# print(voices)

# Speaking
def speak(text):
    engine.say(text)
    engine.runAndWait()

todayDate = datetime.datetime.now()

# Retrieves audio from a microphone
r = sr.Recognizer()

print("Assistant: Hey user! This is your assistant speaking. What would you like to call me? Just say a single word.")
speak("Hey user! This is your assistant speaking. What would you like to call me? Just say a single word.")

# Capturing the name for itself
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print(" ")
    print("-- Assistant is listening --")
    print(" ")
    audio = r.listen(source)
    name = r.recognize_google(audio)
    print("Malhar: " +name)

print(f"{name}: {name} seems to be a good name. So, how have you been?")
speak(f"{name} seems to be a good name. So, how have you been?")

# == Initial Greeting, not a necessary part ==

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print(" ")
    print(f"-- {name} is listening --")
    print(" ")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("Malhar: " +text)

if "what" and "about" and "you" in text:
    print(f"{name}: I am having a good day Malhar.")
    speak("I am having a good day Malhar.")

# == Main functionalities, a necessary part ==
    
print(f"{name}: How can I be of any assistance to you today?")
speak("How can I be of any assistance to you today?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print(" ")
    print(f"-- {name} is listening --")
    print(" ")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print("Malhar: " +text2)

if "information" in text2:
    print(f"{name}: Which topic would you like me to look up for?")
    speak("Which topic would you like me to look up for?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print(" ")
        print(f"-- {name} is listening --")
        print(" ")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print("Malhar: " +infor)
    
    print(f"{name}: Accesing Google for {infor}...")
    speak(f"Accesing Google for {infor}...")
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    print(f"{name}: Which video do you want me to play?")
    speak("Which video do you want me to play?")
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print(" ")
        print(f"-- {name} is listening --")
        print(" ")
        audio = r.listen(source)
        video = r.recognize_google(audio)
        print("Malhar: " +video)

    print(f"{name}: Accessing YouTube for {video}")
    speak(f"Accessing YouTube for {video}")
    assist = music()
    assist.play(video)

elif "news" or "updates" or "updates" in text2:
    print(f"{name}: Accessing the news...")
    speak("Accessing the news..")
    arr = news()
    for i in range(len(arr)):
        print(f"{name}: " +arr[i] +" ")
        speak(arr[i])

elif "fact" in text2 or "facts" in text2:
    print(f"{name}: Sure, here's one, just for you.")
    speak("Sure, here's one, just for you.")
    x = randfacts.get_fact()
    print(f"{name}: Did you know that " +x)
    speak("Did you know that " +x)

elif "joke" in text2 or "jokes" in text2 or "laugh" in text2:
    print(f"{name}: Yup, I can do that.")
    speak("Yup, I can do that.")
    arr = joke()
    print(f"{name}: " +arr[0])
    speak(arr[0])
    print(f"{name}: " +arr[1])
    speak(arr[1])

elif "translate" in text2 or "translation" in text2:

    print(f"{name}: Which language would you like to translate from?")
    speak("Which language would you like to translate from?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print(" ")
        print(f"-- {name} is listening --")
        print(" ")
        audio = r.listen(source)
        source = r.recognize_google(audio)
        print("Malhar: " +source)

    print(f"{name}: Which language would you like to translate to?")
    speak("Which language would you like to translate to?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print(" ")
        print(f"-- {name} is listening --")
        print(" ")
        audio = r.listen(source)
        target = r.recognize_google(audio)
        print("Malhar: " +target)

    print("{name}: What would you like to translate?")
    speak("What would you like to translate?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print(" ")
        print(f"-- {name} is listening --")
        print(" ")
        audio = r.listen(source)
        content = r.recognize_google(audio)
        print("Malhar: " +content)

    translate_text(target, source, content)