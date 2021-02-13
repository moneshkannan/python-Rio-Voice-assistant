# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:44:57 2021

@author: monesh kannan
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def pick_up_command():
    try:
        with sr.Microphone() as source:
            print("i am catching your voice please say something")
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            
            command=command.lower()
            if 'rio' in command:
                command = command.replace('rio','')
                print(command)
    except:
        pass
    return command

def run_rio():
    command=pick_up_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who was ' in command:
        person=command.replace('who was', '')
        print(person)
        info = wikipedia.summary(person,1)
        talk(info)
    else:
        print('Please say again!!!!!!!!!!!!!!')

while True:        
    run_rio()