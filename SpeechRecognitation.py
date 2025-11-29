import speech_recognition as sr
import webbrowser
import os

# Initialize text-to-speech
speaker = pyttsx3.init()

# Initialize speech recognizer
recognizer = sr.Recognizer()

speaker.say("Welcome to the Project")
speaker.runAndWait()

with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)  # Reduce noise
    audio = recognizer.listen(source)

    try:
        
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print("You said:", text)

        
        speaker.say(text)
        speaker.runAndWait()

        
        if "open terminal" in text or "open command prompt" in text:
            speaker.say("Opening command prompt")
            speaker.runAndWait()
            os.system("start cmd")

        elif "open chrome" in text:
            speaker.say("Opening Chrome")
            speaker.runAndWait()
            
            webbrowser.open("https://www.google.com")

        elif "open google" in text:
            speaker.say("Opening Google")
            speaker.runAndWait()
            webbrowser.open("https://www.google.com")

    except Exception as e:
        print("Error:", e)
        speaker.say("I could not understand what you said.")
        speaker.runAndWait()
