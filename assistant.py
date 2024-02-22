
#pls note , i stopped this project , it is guaranteed to have wierd code in it 


import speech_recognition as sr
import pyttsx3
import wikipediaapi
from datetime import datetime
from clss import Name

def speak(text):

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_wikipedia_summary(item):

    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(item)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find any information about that."

def main():

    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        print("Listening...")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio).lower()
            print("You said:", command)

            if "hi" in command:
                speak("Hello! How can I assist you  today?")

            elif "day" in command:
                today = datetime.now().strftime("%A")
                speak(f"Today is {today}.")

            elif "time" in command:
                now = datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {now}.")
            elif "hello" in command:
                  print("numbers")
                  with mic as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                  try:
                     print("Recognizing...")
                     command = r.recognize_google(audio).lower()
                     print("You said:", command)
                     while "add" in command:
                        if "one" in comamnd:
                            speak("w")
                  except:
                      print("s")

            # elif "summary of" in command:
            #     item = command.replace("summary of", "").strip()
            #     summary = get_wikipedia_summary(item)
            #     speak(f"Here is a summary of {item}: {summary}")

            elif "exit" in command:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I didn't understand that. Please try again.")

        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError:
            print("Error with the speech recognition service.")

if __name__ == "__main__":
    main()
