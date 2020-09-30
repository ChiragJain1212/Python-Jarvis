#Module
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


#Intro
engine = pyttsx3.init()
engine.say("How may i help You")
engine.runAndWait()

#Wishing function




#Microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("How may I help You")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print ("You said: {}".format(text))
    except:
        print("Sorry")
    #opening google
if 'open Google' in text:
    webbrowser.open("www.google.com")
    engine.say("Opening Google")
    print ("Opening Google")
    engine.runAndWait()

#open yioutube
if 'open YouTube' in text:
    webbrowser.open("www.youtube.com")
    engine.say("Opening Youtube")
    print ("Opening Youtube")
    engine.runAndWait()

#to search any thing on wikipedia
if 'Wikipedia' in text:
    engine.say('Searching Wikipedia...')
    text = text.replace("wikipedia", "")
    results = wikipedia.summary(text, sentences=2)
    engine.say("According to Wikipedia")
    print(results)
    engine.say(results)
    engine.runAndWait()
#
if 'who are you' in text:
    engine.say("I am Jarvis")
    print ("I am Jarvis")
    engine.runAndWait()

#opening installed app
if 'open sublime' in text:
    webbrowser.open("C:\Program Files (x86)\Sublime Text 3\sublime_text.exe")
    print ("opening")
    engine.say("OPENING SUBLIME")
    engine.runAndWait()

#opening python official website
if 'open python' in text:
    webbrowser.open("python.org")
    engine.say("opening python .org")
    engine.runAndWait()

#opening calculator
if 'turn on calculator' in text:
    engine.say("Turning on Calculator")
    engine.runAndWait()
    print ("Turning on Calcultor")
    print ("enter num1")
    a = input()
    print ("enter num2")
    b = input()
    print (a+b)

# for playing music
if 'open gaana' in text:
    engine.say("OPENING GAANA")
    webbrowser.open("www.gaana.com")
    engine.runAndWait()

#opening yahoo! mail
if 'open my mailbox' in text:
    webbrowser.open("https://in.yahoo.com/?p=us")
    print ("Opening your Mailbox")
    engine.say("OPENING YOUR MAILBOX")
    engine.runAndWait()
#for opening school website
if 'open my School website' in text:
    webbrowser.open('www.subodhpublicschool.com')

#opening Flipkart
if 'open Flipkart' in text:
    print ("Opening Flipkart...")
    engine.say("Opening Flipkart")
    engine.runAndWait()
    webbrowser.open("www.flipkart.com")

#opening wimpy kid
if 'open Wimpy Kid' in text:
    print ("Opening...")
    engine.say("OK")
    webbrowser.open("www.wimpykidclub.com")

#opening pycharm
if 'open Pycharm' in text:
    webbrowser.open("your path")

#opening powershell


#opening Scratch 2
if 'open scratch' in text:
    engine.say("Opening Scratch")
    print ("Opening Scratch")
    webbrowser.open("your path")

#opening Chrome
if 'open Chrome' in text:
    print ("Opening Chrome...")
    engine.say("Opening Chrome...")
    webbrowser.open("Your Chrome path")

#jarvis
if 'Jarvis' in text:
    print ("Yes")
    engine.say("Yes")
    engine.runAndWait()

if 'who made you' in text:
    engine.say("Chirag Jain")
    print ("Chirag Jain")
    engine.runAndWait()

#Hindi Version