import pyttsx3
import speech_recognition as sr


engine=pyttsx3.init()

def speek(text):
     voices=engine.getproperty('voices')
     #print(voices)
     engine.setproperty('voice', voices[0].id)
     engine.say(text)
     engine.runAndWait()

speek("Hello eneryone")

def recvoice():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say something.........")
            r.pause_threshold = 1
            audio = r.listen(source)
    except Exception as e:
        print("Microphone not found.....")
        print(e)
    try:
        print("calculating..........")
        query = r.recognize_google(audio, language= 'en-in')
        print(query)
        return query
    except Exception as e:
        print("Say that again ????")
text="Hi"
while text!="exit":

    text = recvoice()
    speek(text)