# In this project, I'll be incorporating speech-to-text, text-to-speech, and personal voice assistance functionalities into a single Python script file (STV).

# If you are looking for a project that deals with converting speech and text, you can refer to the libraries mentioned above. I have created a file called texttospeech.py

# For the personal voice assistance component, you can find it in the PVA.py file.

Before running the program, it's essential to pre-install the following libraries. To do this, simply copy the library names and paste them into the command "pip install <package_name>":
from ast import Import -->  Abstract Syntax Trees (AST) Import

from email.mime import audio --> Email Audio Handling

from tkinter import * --> Graphical User Interface (GUI) for Tkinter

from tkinter.messagebox import showinfo --> Message Box Display for Tkinter

from gtts import gTTS, gTTSError --> Text-to-Speech Conversion with gTTS (Google Text-to-Speech)

import speech_recognition as sr --> Speech Recognition

import playsound as p --> Sound Playback

import webbrowser --> Web Browsing Functionality

from smtplib import * --> Sending Emails using SMTP

