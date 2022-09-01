import speech_recognition as sr
from talk import talk
import wikipedia
import features as my
from details import *
"""
Maya the virtual Assistant.
By Ilesanmi Oluwasijibomi
-----------------------------Notes ----------------------------------
1. Because siji is a bad programmer, in this code Nonetype == 0, to return Nonetype in programs.

"""
listener = sr.Recognizer()
close = 0

def takecommand():
    command = ''
    try:
        with sr.Microphone() as source:
            talk('Maya,  is listening ...')
            # print('Listening...')
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
    if 'play' in command:my.mayaplaysong(command)
    elif 'time' in command:my.mayatime()  
    elif 'close' in command: 
        global close
        close = 1
    
    elif 'define ' in command or 'what is ' in command:
        # my.wikidefine(command)
        info  =  command.replace('define ', '')
        answer = wikipedia.summary(info,2)
        talk (answer)


def main():
    while True:
        run_maya()
        global close
        if close == 1:
            talk('Maya is switching off.')
            break
    print('Maya is switching off.')
    return

main()
