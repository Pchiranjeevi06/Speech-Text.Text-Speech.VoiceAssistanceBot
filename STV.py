from ast import Import
from email.mime import audio
from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS,gTTSError
import speech_recognition as sr
import os
import re
import playsound as p
import webbrowser
from smtplib import *

mainwindow= Tk()
mainwindow.title('\nText-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='#FFCC99')

num = 1
def sofiaResponse(audio):
    global num
    num += 1
    toSpeak = gTTS(text = audio, lang ='en', slow = False)
	    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
        # playsound package is used to play the same file.
    p.playsound(file, True)
    os.remove(file)
    return text1.insert(END,"sofia :\n"+str(audio)+"\n")
class base:
    def say(text1):
        language = 'en'
        speech = gTTS(text = text1, lang = language, slow = False,tld="com")
        speech.save("text.mp3")
        os.system("start text.mp3")

    #Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
    def myCommand() :
        while True:
            global command
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Say something...')       
                audio = r.listen(source,phrase_time_limit = 3)
                print("stop")
            try:
                command = r.recognize_google(audio,language ='en-IN')
                print('Converting audio transcripts into text ...')
                print('You said: ' + command + '\n')
    
            except sr.UnknownValueError:
                sofiaResponse("....")
                break
        return command
        
            
class program_Execution:
    def assistant(command):
        if 'open' in command:
            reg_ex = re.search('play(.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.youtube.com/results?search_query='+"+".join(domain)
                sofiaResponse("opening "+domain+" on YouTube")
                webbrowser.open(url)
                
        elif 'wikipedia search' in command:
            reg_ex = re.search('wikipedia search (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)  
                url="https://en.wikipedia.org/wiki/" + domain
                sofiaResponse('opening in wikipedia')
                webbrowser.open(url)
        elif 'search' in command:
            reg_ex = re.search('search (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)  
                url="https://www.google.com/search?q=" + '+'.join(domain)
                sofiaResponse('these '+domain+' search results came')
                webbrowser.open(url)

        elif 'email' in command:
            sofiaResponse('Who is the recipient?')
            recipient = base.myCommand()
            if 'chiru' in recipient:
                sofiaResponse('What should I say to him?')
                content = base.myCommand()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('your_email_address', 'your_password')
                mail.sendmail('sender_email', 'receiver_email', content)
                mail.close()
                sofiaResponse('Email has been sent successfuly. You can check your inbox.')
            else:
                sofiaResponse('I don\'t know what you mean!')
        elif "launch" in command:
           reg_ex = re.search('launch (.*)', command.lower())
           if reg_ex:   
                appname = reg_ex.group(1)
                if appname=="whatsapp":
                    t=r"C:\Users\CHIRANJEEVI\AppData\Local\WhatsApp\Whatsapp.exe"
                elif appname=="msedge":
                    t="C:/Program Files (x86)/Microsoft/Edge/Application/"+appname+".exe"
                elif appname=="firefox":
                    t="C:/Program Files/Mozilla Firefox/firefox.exe"
                elif appname =="vlcplayer":
                    t=r"C:\Program Files\VideoLAN\VLC\vlc.exe"
                elif appname=="excel":
                    t=r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.lnk"
                
                sofiaResponse('launching '+appname)
                os.startfile(t)
class speeh2text_text2speech:
    def TextToSpeech():
        texttospeechwindow = Toplevel(mainwindow)
        texttospeechwindow.title('Text-to-Speech Converter')
        texttospeechwindow.geometry("500x500")
        texttospeechwindow.configure(bg='#FFC0CB')

        Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Times New Roman", 15), bg='#808080',fg="#FFFFFF").place(x=50)
        text = Text(texttospeechwindow, height=5, width=55, font=9)
        text.place(x=7, y=60)


        speakbutton = Button(texttospeechwindow, text='Play', bg='coral', command=lambda: base.say(str(text.get(1.0, END))))
        speakbutton.place(x=140, y=200)

    def SpeechToText():
        
        speechtotextwindow = Toplevel(mainwindow)
        speechtotextwindow.title('Speech-to-Text Converter ')
        speechtotextwindow.geometry("500x500")
        speechtotextwindow.configure(bg='#FFC0CB')     
        Label(speechtotextwindow, text='Speech-to-Text Converter ', font=("Comic Sans MS", 8), bg='yellow').place(x=50)     
        text = Text(speechtotextwindow, font=8, height=7, width=45)  
        text.place(x=7, y=100)     
                
            
        recordbutton = Button(speechtotextwindow, text='change', bg='orange', command=lambda:text.insert(END, base.myCommand()))
        recordbutton.place(x=140, y=50)
        
    def voiceframe():
        global text1
        voicewindow = Toplevel(mainwindow)
        voicewindow.title('Personal Voice Assistance')
        voicewindow.geometry("500x500")
        voicewindow.configure(bg='#FFC0CB')     
        Label(voicewindow, text='Personal Voice Assistance ', font=("Comic Sans MS", 14), bg='pink').place(x=60)     
        text1 = Text(voicewindow, font=5, height=30, width=55)
        text1.place(x=2, y=42)    
        
        recordbutton = Button(voicewindow, text='voice', bg='green',fg="white", command=voiceinput)
        recordbutton.place(x=350, y=10)

def voiceinput():
    sofiaResponse("Hii, this is Assistance \nWhat's your name, Dude.")
    name = base.myCommand()
    sofiaResponse("Hello, " + name + '.')
    while True :   
        sofiaResponse("How can I help you?")         
        text = base.myCommand().lower() 
        if text == " ": 
            continue 
        if "exit" in command or "bye" in command or "sleep" in command:
            sofiaResponse("Ok bye,have a nice day,"+ name+'.')
            break
        program_Execution.assistant(text)    
     

Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='#ADD8E6', wrap=True, wraplength=450,).place(x=25, y=0)


texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='#CAF1DE', command=speeh2text_text2speech.TextToSpeech)
texttospeechbutton.place(x=100, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='#CAF1DE', command=speeh2text_text2speech.SpeechToText)
speechtotextbutton.place(x=100, y=250)

textbutton = Button(mainwindow, text='voice assistance', font=('Times New Roman', 16), bg='#CAF1DE', command=speeh2text_text2speech.voiceframe,padx=50)
textbutton.place(x=100, y=350)

mainwindow.update() 
mainwindow.mainloop()
