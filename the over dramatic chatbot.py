from winsound import PlaySound
import os
from PIL import Image as img
import pyttsx3
while True:
    

    def ok():
        o=img.open('me.png')
        o.show()
        return ok
    def m():
        m=img.open('astro.jpg')
        m.show()
        speak("hello world")
        return m
    
    def ironman():
        m=img.open('ironman.jpg')
        m.show()
        os.startfile('ironman.mp3')
        return ironman

    def control():
        m=img.open('Control.jpg')
        m.show()
        os.startfile('control.mp3')
        return control

    def udaymajnu():
        m=img.open('udaymajnu.jpg')
        m.show()
        os.startfile('Uday Majnu.mp3')
        return udaymajnu

    def bond():
        m=img.open('bond.jpg')
        m.show()
        os.startfile('bond.mp3')
        return bond

    def love():
        m=img.open('i love you.jpg')
        m.show()
        os.startfile('I LOVE YOU.mp3')
        return love

    def speak(command):

        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    
    bot=input("hello there write something ")

    if bot=='hello':
        m()

    elif 'love you 3000' in bot:
        ironman()

    elif bot=='madar chood':
        control()

    elif bot=='who are you':
        udaymajnu()

    elif bot=='i love you':
        love()