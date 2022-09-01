import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id )
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()