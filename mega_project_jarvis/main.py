import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


engine = pyttsx3.init()
newsapi = "44c6abf73f304d4c9e8297817de4834c"

def speak(text):
  engine.say(text)
  engine.runAndWait()
def processCommand(command):
    print(command)
    if("open google"in command.lower()):
        webbrowser.open("https://google.com")
    elif("open facebook" in command.lower()):
        webbrowser.open("https://facebook.com")
    elif("open chat gpt" in command.lower()):
        webbrowser.open("https://chatgpt.com/")
    elif("open github"  in command.lower()):
        webbrowser.open("https://github.com")
    elif("open linkedin"in command.lower()):
        webbrowser.open("https://linkedin.com")
    elif("open youtube"in command.lower()):
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
         try:
            song = command.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
         except KeyError:
             speak("Sorry sir,I Dont have this song in my library")
    elif "news" in command.lower():
        r =  requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])        
        
if __name__ == "__main__":
    speak("INITIALIZING FRIDAY")
    #LISTENING FOR THE WAKE WORD JARVIS
    while True:
      # Microphone se input lena
          r = sr.Recognizer()
          print("listening...")
          try:
            with sr.Microphone() as source:
              # Google Speech Recognition API se text me convert karo
                  print("processing...")
                  audio = r.listen(source,timeout=2,phrase_time_limit=1)
                  command = r.recognize_google(audio, language='en-US') 
                  if(command.lower() == "friday"):
                    speak("YES SIR")
                    print("Give Command")
                    with sr.Microphone() as source:
                        audio = r.listen(source,timeout = 5,phrase_time_limit = 2)
                        command = r.recognize_google(audio,language = 'en-US')
                        processCommand(command)

                    #NOW LISTENING FOR COMMAND
          except sr.UnknownValueError:
              print("Samajh nahi aaya, thoda clearly bolo.")
          except sr.WaitTimeoutError:
              print("Timeout: Tumne kuch bola hi nahi.")
          except sr.RequestError as e:
              print(f"Request error: {e}")
