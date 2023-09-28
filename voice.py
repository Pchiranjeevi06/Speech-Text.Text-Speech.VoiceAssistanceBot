from email.mime import audio
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
from time import strftime
import playsound as p
import subprocess
from gtts import gTTS
import wikipedia
import wolframalpha # to calculate strings into formula

num = 1
def sofiaResponse(audio):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	print("Person : ", audio)

	toSpeak = gTTS(text = audio, lang ='en', slow = False,tld="com")
	# saving the audio file given by google text to speech
	file = str(num)+".mp3"
	toSpeak.save(file)
	
	# playsound package is used to play the same file.
	p.playsound(file, True)
	os.remove(file)

def myCommand():
    global command
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')       
        audio = r.listen(source,phrase_time_limit = 5)
        print("stop")
    try:
        command = r.recognize_google(audio,language ='en-US')
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command



def assistant(command):
    if 'open' in command:
        
        sofiaResponse("Opening Wikipedia")
        indx = command.lower().split().index(command.remove("open"))
        query = command.split()[indx + 1:]
        url="https://en.wikipedia.org/wiki/" + '_'.join(query)
        webbrowser.open(url)
        sofiaResponse('opening '+command)
        
    elif 'launch' in command:
        reg_ex = re.search('launch\s+(.*)', command)
        if reg_ex:
            appname = reg_ex.group(1)
            appname1 = appname+".app"
            subprocess.Popen(["open", "-n", "/Program Files/Google/Chrome/Application" + appname1], stdout=subprocess.PIPE)
            sofiaResponse('I have launched the desired application')
            
    elif "calculate" in command:
        app_id = "WOLFRAMALPHA_APP_ID"
        client = wolframalpha.Client(app_id)
        indx = audio.lower().split().index('calculate')
        query = audio.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text 
        sofiaResponse("The answer is " + answer) 
        return answer

sofiaResponse("Hey, this is Assistance \nWhat's your name, Dude.")
name = myCommand()
sofiaResponse("Hello, " + name + '.')
while True :   
    sofiaResponse("How can I help you?")
    assistant(myCommand())     
    text = myCommand().lower() 
    if text == " ": 
        continue 
      
    if "exit" in command or "bye" in command or "sleep" in command:
        sofiaResponse("Ok bye,have a nice day,"+ name+'.')
        break
          

            