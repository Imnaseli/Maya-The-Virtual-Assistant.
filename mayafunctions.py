"""
All of Mayas Functions are going to be stored here for Reuse.
details.py has some useful iterables used in maya.py yhis script.
"""
import pywhatkit
import datetime
from details import *
import wikipedia
from maya import *
from maya import talk

#Play Music from YouTube.
def mayaplaysong(command):
    for word in playsongwords:
        if word in command:
            song = command.replace(word , '')
    print (f'Playing {song} ...')
    talk (f'Playing {song} ...')
    pywhatkit.playonyt(song)

def mayatime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('The current time is,' ,  time)
    
def wikidefine(command , phrase):
    info = command.replace(phrase , '')
    answer = wikipedia.summary(info , 1)
    talk(answer)
    
    