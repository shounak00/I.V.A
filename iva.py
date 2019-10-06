import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import googlesearch
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello Sir, I am IVA. How can I help you?")   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
''' 

if __name__ == "__main__":
    
    wishMe()
    while True:
    
        query = takeCommand().lower()
        
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)

        if 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("youtube.com")

        if 'open google' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("google.com")

        if 'open stackoverflow' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'google ' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.google.com/search?q='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(search_url)
        
        elif 'youtube ' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.youtube.com/results?search_query='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(search_url)      

        elif 'play music' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'open code blocks' in query:
            codebPath = 'C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            os.startfile(codebPath)  

        if 'terminate' in query:
            exit()
        if 'quit' in query:
            exit()
        
        
        



