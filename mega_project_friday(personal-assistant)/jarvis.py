import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import subprocess
import time
import re
import threading


question = ["what","how","when","where","tell me","can you","who"]
engine = pyttsx3.init()
speaking = False
newsapi = "44c6abf73f304d4c9e8297817de4834c"
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

    
def speak(text):
  engine.say(text)
  engine.runAndWait()
def clear_response(statement):
     return re.sub(r"[*_`]+", "", statement)
def ask_local_llm(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2:latest",  # change this if you installed another model like deepseek
        "prompt": prompt,
        "stream": False     # stream False means full response in one go
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return "Sorry bhai, model se response nahi aaya."
    except Exception as e:
        return f"LLM error: {e}"

def close_process_with_grace(process_name, wait_seconds=5):
    # Step 1: Gracefully close (taskkill without /F)
    subprocess.run(["taskkill", "/IM", process_name], shell=True)
    print(f"Sent close signal to {process_name}, waiting {wait_seconds} seconds...")

    # Step 2: Wait for process to close
    time.sleep(wait_seconds)

    # Step 3: Force kill (taskkill with /F)
    # This will ensure process is terminated if still running
    subprocess.run(["taskkill", "/F", "/IM", process_name], shell=True)
    print(f"Force kill command sent to {process_name} (if still running).")

def processCommand(command):
    print(command)
    if("open google"in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://google.com")
    elif("open facebook" in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://facebook.com")
    elif("open chat gpt" in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://chatgpt.com/")
    elif("open github"  in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://github.com")
    elif("open linkedin"in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://linkedin.com")
    elif("open youtube"in command.lower()):
        speak(f"opening {command.split(' ')[1]}")
        webbrowser.open("https://youtube.com")
    elif("open portfolio"in command.lower()):
        speak(f"opening your {command.split(' ')[1]}")
        webbrowser.open_new_tab("https://helpful-elf-967c0f.netlify.app/")
    elif("open whatsapp"in command.lower()):
        speak(f"opening your {command.split(' ')[1]}")
        subprocess.run(["start", "whatsapp:"], shell=True)
    elif("close browser"in command.lower()):
        speak(f"closing {command.split(' ')[1]}")
        close_process_with_grace("brave.exe", wait_seconds=5)
    elif("close whatsapp"in command.lower()):
        speak(f"closing {command.split(' ')[1]}")
        close_process_with_grace("WhatsApp.exe", wait_seconds=5)
    elif command.lower().startswith("play"):
         try:
            song = command.lower().split(' ')[1]
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

    else:
      for word in question:
        if word in command:
              speak("Processing with my brain sir please wait.")
              answer = ask_local_llm(command)
              speak(clear_response(answer))
              speak("next question sir")
      
        
if __name__ == "__main__":
    speak("INITIALIZING JARVIS")
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
                  if(command.lower() == "jarvis"):
                    speak("YES BOSS")
                    print("Give Command")
                    with sr.Microphone() as source:
                        audio = r.listen(source,timeout = 2,phrase_time_limit = 5)
                        command = r.recognize_google(audio,language = 'en-US')
                        processCommand(command)

                    #NOW LISTENING FOR COMMAND
          except sr.UnknownValueError:
              print("Samajh nahi aaya, thoda clearly bolo.")
          except sr.WaitTimeoutError:
              print("Timeout: Tumne kuch bola hi nahi.")
          except sr.RequestError as e:
              print(f"Request error: {e}")
