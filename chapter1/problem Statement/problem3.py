import pyttsx3

engine = pyttsx3.init()

text = "Hello Priyansh!"

engine.say(text)

engine.runAndWait()