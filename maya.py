import speech_recognition as sr
import pyttsx3
from details import *
import pywhatkit
# from mayafunctions import *
from mayafunctions import mayaplaysong, mayatime , wikidefine

"""
Maya the virtual Assistant.
By Ilesanmi Oluwasijibomi
----------- Notes -----------
1. Because siji is a bad programmer, in this code Nonetype == 0, to return Nonetype in programs.

"""

engine = pyttsx3.init()
listener = sr.Recognizer()

#To give Maya a female voice
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id )


close = False

#Maya talk funtion for her to speak.
def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    try:
        with sr.Microphone() as source:
            talk('Maya,  is all ears ...')
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()            
            if 'maya' in command:
                command = command.replace('maya '  , '')
                print(command)
    except:
        pass
    return command
    


def run_maya():
    command = takecommand()
    if 'play' in command: mayaplaysong(command)
    elif 'time' in command: mayatime()      
    elif 'close' or 'end' in command: close = True
    
    elif '' in command:
        for phrase in wikipediaphrase:
            if phrase in command: wikidefine(command , phrase)
            else:pass
        
        
while True:
    run_maya()
    if close == True:
        talk('Maya is switching off.')
        break