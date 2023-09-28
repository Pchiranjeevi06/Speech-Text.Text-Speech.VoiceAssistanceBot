# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations

num = 1
def assistant_speaks(output):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	print("Person : ", output)

	toSpeak = gTTS(text = output, lang ='en', slow = False)
	# saving the audio file given by google text to speech
	file = str(num)+".mp3"
	toSpeak.save(file)
	
	# playsound package is used to play the same file.
	playsound.playsound(file, True)
	os.remove(file)



def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")
		
		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit = 5)
	print("Stop.") # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language ='en-US')
		print("You : ", text)
		return text

	except:

		assistant_speaks("Could not understand your audio, Please try again !")
		return 0


# Driver Code

def process_text(input):
	try:
		if 'search' in input or 'play' in input:
			# a basic web crawler using selenium
			search_web(input)
			return

		elif "who are you" in input or "define yourself" in input:
			speak = '''Hello, I am ThunderBolt. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak)
			return

		elif "who made you" in input or "created you" in input:
			speak = "I have been created by Group named The Midnight Oil Burners."
			assistant_speaks(speak)
			return

		elif "geeksforgeeks" in input:# just
			speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
			assistant_speaks(speak)
			return

		elif "calculate" in input.lower():
			
			# write your wolframalpha app_id here
			app_id = "WOLFRAMALPHA_APP_ID"
			client = wolframalpha.Client(app_id)

			indx = input.lower().split().index('calculate')
			query = input.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			assistant_speaks("The answer is " + answer)
			return

		elif 'open' in input:
			
			# another function to open
			# different application available
			open_application(input.lower())
			return

		else:

			assistant_speaks("I can search the web for you, Do you want to continue?")
			ans = get_audio()
			if 'yes' in str(ans) or 'yeah' in str(ans):
				search_web(input)
			else:
				return
	except :

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
		ans = get_audio()
		if 'yes' in str(ans) or 'yeah' in str(ans):
			search_web(input)
def search_web(input):

	driver = webdriver.Firefox()
	driver.implicitly_wait(1)
	driver.maximize_window()

	if 'YouTube' in input.lower():

		assistant_speaks("Opening in youtube")
		indx = input.lower().split().index('YouTube')
		query = input.split()[indx + 1:]
		driver.get("https://www.youtube.com/watch?v=CC6IvcL-F_8" + '+'.join(query))
		return 

	elif 'wikipedia' in input.lower():

		assistant_speaks("Opening Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

		return


# function used to open application
# present inside the system.
def open_application(input):

	if "chrome" in input:
		assistant_speaks("Google Chrome")
		os.startfile('C:\Program Files\Google\Chrome.exe')
		return

	elif "edge" in input or "internet explorer" in input:
		assistant_speaks("Opening Microsoft Edge")
		os.startfile('C:\Program Files (x86)\Microsoft\Edge\Application\microsoftedge.exe')
		return

	elif "word" in input:
		assistant_speaks("Opening Microsoft Word")
		os.startfile('C:\Program Files\Microsoft Office\root\Office16\\WINWORD.lnk')
		return

	elif "excel" in input:
		assistant_speaks("Opening Microsoft Excel")
		os.startfile('C:\Program Files\Microsoft Office\root\Office16\\Excel.lnk')
		return

	else:

		assistant_speaks("Application not available")
		return
if __name__ == "__main__":
	assistant_speaks("Hii, this is Assistance \nWhat's your name, Dude.")
	name ='Dude'
	name = get_audio()
	assistant_speaks("Hello, " + name + '.')
	
	while(1):

		assistant_speaks("What can i do for you?")
		text = get_audio().lower()

		if text == 0:
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
			assistant_speaks("Ok bye, See you Again,"+ name+'.')
			break

		# calling process text to process the query
		process_text(text)