import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    if (speak == ""):
        raise NameError("TypeError: speak("") is empty")
    engine.say(audio)
    engine.runAndWait()