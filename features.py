"""
All of Mayas Functions are going to be stored here for Reuse.
details.py has some useful iterables used in maya.py yhis script.
"""

import pywhatkit
import datetime
import wikipedia
from details import *
from talk import talk

def mayaplaysong(command):
    for word in playsongwords:
        if word in command:
            song = command.replace(word , '')
    print (f'Playing {song} ...')
    talk (f'Playing {song} ...')
    pywhatkit.playonyt(song)
    
def mayatime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f'The current time is, {time}')
    print(f'The current time is, {time}')
    
def wikidefine(command ):
    for word in wikipediaphrase:
        if word in command:
            info = command.replace(word , '')
    answer = wikipedia.summary(info , 2)
    print(answer)
    talk(answer)
    