import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mac' in command:
                command = command.replace('mac', '')
                print(command)
    except:
        pass
    return command


def run_macAi():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        speak("the time is")
        time()
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        speak(info)
    elif 'date' in command:
        speak("the date is")
        date()
    elif 'are you single' in command:
        speak('I am in a relationship with wi-fi') 
    elif 'who are you' in command:
        speak('I am mac, a courtesy of Meshack')
    elif 'siri' in command:
        speak('yeah; Only that our relationship is professional')
    elif 'cortana' in command:
        speak('i have only heard of her in halo')
    
    elif 'where can i hide a dead body' in command:
        speak("i'll call nine one one")
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    else:
        speak('I cant get you well. Please repeat.')


while True:
    run_macAi()
