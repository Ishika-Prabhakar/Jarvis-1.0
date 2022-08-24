import pyaudio
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os




engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
     speak('Hello! ')
     

     hour=datetime.datetime.now().hour

     if hour>=6 and hour<12:
         speak("good morning ishika!")
     elif hour>=12 and hour<=18:
         speak("good afternoon ishika")
     elif hour>18 and hour<=24:
         speak("good evening ishika ")
     else:
         speak("good night ishika")
     speak("Jarvis at your service. Please tell me how can i help you ?")
         



def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ishika.prabhakar@gmail.com','Ishika@2002')
    server.sendmail('username@gmail.com',to,content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())




if __name__=='__main__':
    wishme()


    while True:
        query = TakeCommand().lower()

        if 'time' in query:
             time_()
        if 'date' in query:
             date_()
        if 'wikipedia' in query:
             speak('speaking...')
             query=query.replace('wikipedia','')
             result = wikipedia.summary(query,sentences=3)
             speak('according to wikipedia')
             print(result)
             speak(result)
        if 'thank you' in query:
              break       
        if 'good night' in query:
             speak('good night ishika')
             break
        if 'send email' in query:
            try:
                speak('what should i say?')
                content = TakeCommand()
                speak('who is the reciever?')
                reciever = input("enter reciever's email")
                to= reciever
                sendEmail(to,content)
                speak(content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("Unable to send email.")

        if 'search in brave' in query:
            speak('what should i search')
            bravepath = "/usr/share/applications %s"


            search=TakeCommand().lower()
            wb.get(bravepath).open_new_tab(search+".com")
            
        elif 'search in youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)
        elif 'search in google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching....')
            wb.open('https://www.google.com/webhp'+search_Term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'go offline' in query:
            speak("going offline")
            quit()
        elif 'vs code' in query:
            speak("Opening vs code........")
            vs_code = r'/home/ishika/Downloads'
            os.startfile(vs_code)