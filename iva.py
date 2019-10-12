import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import googlesearch
import webbrowser
import os
import smtplib
import requests
import sys
import re
import subprocess
import json
import random
import shutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour <12:
        speak("Good Morning Sir")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour<21:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("I am IVA. How can I help you?")   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        return "none"
    
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Yourmail', 'Enter password here')
    server.sendmail('Yourmail', to, content)
    server.close()
 

if __name__ == "__main__":
    
    wishMe()
    while True:
    
        query = takeCommand().lower()
        
        #logic for executing tasks based on query
        if 'wikipedia' in query or "tell" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            #speak("According to Wikipedia")
            #print(results)
            speak(results) 

        if 'open youtube' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening Youtbe")
            webbrowser.get(chrome_path).open("youtube.com")

        if 'open google' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening Google")
            webbrowser.get(chrome_path).open("google.com")        

        elif 'open project' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening your github sir")
            webbrowser.get(chrome_path).open("https://github.com")
        
        elif 'open trello' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening your trello board sir")
            webbrowser.get(chrome_path).open("https://trello.com/shounaksobahani/boards")
        
        elif 'health' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.webmd.com/search/search_results/default.aspx?query='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("Opening WebMd.com")
                webbrowser.get(chrome_path).open(search_url)
      
        elif 'buy' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.daraz.com.bd/catalog/?q='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("Opening online shop")
                webbrowser.get(chrome_path).open(search_url)
        
        elif 'research' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://scholar.google.com/scholar?q='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("Opening Google scholar publications Sir")
                webbrowser.get(chrome_path).open(search_url)

        elif 'open stackoverflow' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening Stack Overflow")
            webbrowser.get(chrome_path).open("stackoverflow.com")
        
        elif 'open scholar' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening Google Scholar")
            webbrowser.get(chrome_path).open("https://scholar.google.com")

        elif 'google ' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.google.com/search?q='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("Opening Right away")
                webbrowser.get(chrome_path).open(search_url)
        
        elif 'youtube ' in query:
                text = query
                res = text.split(' ', 1)[1]
                url= 'https://www.youtube.com/results?search_query='
                search_url=url+res
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("Opening It Sir")
                webbrowser.get(chrome_path).open(search_url)      

        if 'play music' in query or 'play song' in query:
            music_dir = 'E:\\Songs'
            songs = os.listdir(music_dir)
            speak("Opening Songs")
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        if 'the  time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is ")
            speak(strTime)
        
        if 'email' in query or "help me send a mail" in query:
            try:
                speak("What should I say?")
                content = takeCommand().r.pause_threshold=10
                speak("Whom you want to send? or You just want to perform Test mail")
                to= takeCommand()
                if "test mail" in to:
                    to1= "shounak00@gmail.com"
                    sendEmail(to1, content)
                    speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("Sorry sir, My System failed to complete the task. Please reinitiate instructions again.")

        if 'open code blocks' in query:
            codebPath = 'C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            speak("Opening Codeblocks")
            os.startfile(codebPath)  
                
        if 'open fifa' in query:
            codebPath = 'E:\\Fifa19\\FIFA19.exe'
            speak("Opening Fifa")
            os.startfile(codebPath)  
        
        if "who are you" in query or "define yourself" in query or "introduce yourself" in query: 
            speak("I am Iva. Your Integrated  Virtual  Assistant, I.V.A. I am here to make your life easier. You can command me to perform various tasks ")
  
        if "who made you" in query or "created you" in query: 
            speak("Sir, Stop being stupid! Obviously u made me.")
        
        if "thank you" in query:
            speak("Your welcome,Sir.")
        
        if 'news' in query:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            speak("Opening Daily Star")
            webbrowser.get(chrome_path).open("https://www.thedailystar.net")

        if 'terminate' in query or 'exit' in query or 'sign off' in query or 'quit' in query or 'your job is done' in query:
            speak("Signing off Sir!")
            exit()
        
        
        if 'open code libraries' in query:
            speak("Access Granted on Code Libraries. What do you want me to implement sir?")
            imp = takeCommand().lower()
            while True:
                if 'table' in imp:
                    filename1 = 'C:\\Users\\User\\Desktop\\I.V.A\\Code Library\\Data Structure\\Sparse_Table.cpp'
                    fileA = open(filename1, 'rb')
                    path= 'C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground'
                    os.makedirs(path)
                    filename2 = 'C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\implementedsparsetable.cpp'
                    fileB = open(filename2, 'wb')
                    shutil.copyfileobj(fileA, fileB)
                    speak("Sparse table implemented")
                    fileA.close()
                    fileB.close()
                    speak("Do you want me to open it sir?")
                    op = takeCommand().lower()
                    if 'yes' in op:
                        os.startfile('C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\implementedsparsetable.cpp')
                        speak("The code is opened. Exiting code libraries")
                        break
                    if 'no' in op:
                        speak("exiting code libraries")
                        break
                else:
                    speak("Sorry Sir, You haven't manually implemented that library.")
                    speak("exiting code libraries")
                    break
        
        

        
        if 'web template' in query:
            speak("Access Granted on  Web Templates. What do you want me to implement sir?")
            tmp = takeCommand().lower()
            while True:
                if 'login' in tmp:
    
                    speak("Creating CSS style Sheet")
                    fname1 = 'C:\\Users\\User\\Desktop\\I.V.A\\Templates Web\\DemoLoginPage\\css\\style.css'
                    fa = open(fname1,'rb')
                    path= 'C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\Template Log in\\css'
                    os.makedirs(path)
                    fname2 = 'C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\Template Log in\\css\\style.css'
                    fb = open(fname2,'wb')
                    shutil.copyfileobj(fa, fb)
                    fa.close()
                    fb.close()
                    
                    speak("Creating HTML")
                    fname11 = 'C:\\Users\\User\\Desktop\\I.V.A\\Templates Web\\DemoLoginPage\\index.html'
                    fa1 = open(fname11,'rb')
                    fname22 = 'C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\Template Log in\\login.html'
                    fb2 = open(fname22,'wb')
                    shutil.copyfileobj(fa1, fb2)
                    speak("Template Implementation Complete")
                    fa1.close()
                    fb2.close()
                    speak("Do you want me to open it sir?")
                    op = takeCommand().lower()
                    if 'yes' in op:
                        os.startfile('C:\\Users\\User\\Desktop\\I.V.A\\Coding Ground\\Template Log in\\login.html')
                        speak("HTML is opened. Exiting Web Template Implementation")
                        break
                    if 'no' in op:
                        speak("Exiting Web Template Implementation")
                        break
                else: 
                    speak("Sorry Sir, You haven't manually implemented that library.")
                    speak("Exiting Web Template Implementation")
                    break
        


        



       