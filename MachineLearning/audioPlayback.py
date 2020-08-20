from playsound import playsound
import speech_recognition as sr
import subprocess
from commands import Commander


r = sr.Recognizer()
cmd = Commander()

def say(text):
    subprocess.call('say '+text, shell=True)

def initSpeech():
    print("Listenning...")
    playsound('audio/when.mp3')
    with sr.Microphone() as source:
        print('Say something: ')
        audio = r.listen(source)

    playsound('audio/done-for-you.mp3')

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand")


    print(command)
    for x in {"quit","exit","bye","goodbye","sayonara","stop"}:
        if x in command:
            return False

    cmd.discover(command)
    return True


while initSpeech():
    pass
