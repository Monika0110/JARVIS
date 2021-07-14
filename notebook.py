import pyttsx3
import wikipedia  # to run wikipedia queries
import webbrowser # to open webapps
import os
import smtplib # to send mails
import random
import json
import requests
# to speak we need voice so there is an inbuilt voice in windows we can use this with sapi5
# bu default windows have two voices female and male
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# to set the voice
engine.setProperty('voices', voices[1].id)
def speak(audio):
    # speak function simply speaks the given argument
    engine.say(audio)
    engine.runAndWait()

# A wishme function so pc will wish me on the basis of time
import datetime

def Wishme():
    #specify time
    hour = int(datetime.datetime.now().hour)  # give the current hour from 0 to 24
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("Hello Maam, Jarvis Here!, How may I help you!")


# import the module which helps in recognizing what are you saying
import speech_recognition as sr

def takeCommand():
    # functoin which takes microphone input from user and by recognising it returns string output
    
    r=sr.Recognizer()  # the sr object
    
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 1  # increased the time while someone is taking time before speaking
        r.energy_threshold = 100 # decreasing energy threshold as because i speak very low
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=8,phrase_time_limit=8)
        
    try:
        print("Recognizing...")
        #recognizing what you said
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query,"\n")
        
    except Exception as e:
        print(e)
        print("Please Say that Agian!")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("monikasarswat01@gmail.com","aditi@01")
    server.sendmail("monikasarswat01@gmail.com", to, content)
    server.close()

def readNews():
    speak("News for today")
    # speak("Monika ")
    url= ('https://newsapi.org/v2/top-headlines?'

           'country=us&'
           'category=entertainment&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')
    
    response = requests.get(url)
    text = response.text
    obj = json.loads(text)
    arts = obj['articles']

    for i in range(0, 10):
        speak(arts[i]['title'])
        if(i!=9):
            speak("moving to next headline")

    speak("That's all for today Maam!")
    # for articel in arts:
    #     speak(articel['title'])

if __name__=='__main__':
    #speak("Harry Fucking Styles!")
    
    Wishme()
    
    # a infinite while loop to take commands from you
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Monika\\Music"  # give the path of folder where you have your music
            songs = os.listdir(music_dir)  # will list all songs in that directory
            # print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs))) #open that file giving the directory_name+songname

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")  #making the time string
            speak("Maam the time is",strtime)

        elif 'open code' in query:
            codePath = "C:\\Users\\Monika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to monika' in query:
            try:
                speak("what should i say maam?")
                content = takeCommand()
                to = "2019umt1478@mnit.ac.in"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maam, I could not send your email!")

        
        elif 'open images' in query:
            image_dir = "C:\\Users\\Monika\\fuel meta\\Mine"
            images = os.listdir(image_dir)
            # print(images)
            os.startfile(os.path.join(image_dir,random.choice(images)))

        elif 'read news' in query:
            readNews()
        elif 'quit' in query:
            exit()

