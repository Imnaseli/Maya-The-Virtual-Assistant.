import speech_recognition as sr
import pyttsx3

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
                return command
            else:
                return 0
    except:
        talk('Try again')
        return 0
    


def run_maya():
    command = takecommand()
    if command != 0:
        if 'play' in command:
            print('Playing ...')

        if 'close' in command:
            close = True
    
    else:
        talk('Maya does not understand the command.')
        
        
while True:
    run_maya()
    if close == True:
        talk('Maya is switching off.')
        break