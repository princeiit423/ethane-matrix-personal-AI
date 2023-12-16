import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
print(voices[0].id)
engine.setProperty('voice', voices[0].id) # change voices[1] for female voice 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
          

    else:
        speak("Good Evening!")  

    speak("Hello I am Matrix . Please tell me how can i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'matrix' in query:
            speak('Searching...')
            query = query.replace("matrix", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my knowledge")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("open youtube")
            webbrowser.open("youtube.com")
        elif 'who are you' in query:
            speak("My name is Matrix. speed one tera byte memory one giga byte.I am build from E waste material..................if you want to know more about me say your story")


        elif 'who is your creator' in query :
            speak ('you are my creator sir') 

        elif 'your story' in query :
            speak ("I am created. on Asansol Engineering College Lab. from Electronics Waste.Lots of students of. Electronics and Communication Engineering Department. come together to build me. Special thanks to Sujit Goswami sir. and Shubh Kumar from third year. who leads the team ")     

            
        elif 'can you sing' in query :
            speak ('i cannot sing but i can play songs')       

        elif 'who is your friend' in query :
            speak ('I did not have any friend sir')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'sourav' in query :
            speak ("we miss you buddy!") 

        elif 'who is my brother' in query :
            speak("gautam is your brother sir!")       




        elif 'jarvis are you gay' in query:
            speak("no sir")

        elif 'raja' in query:
            speak ("how are you owaaise")    
            

        elif 'who am i' in query:
            speak ('sir you are the gratest of all time, you build me ')


        elif 'jarvis kya tum dance kar sakte ho' in query :
            speak ('no sir i cannot, i am jarvis its cheap task for me')

        

        elif 'play music' in query:
            music_dir = 'C:\music bollywood' # change path to your music directories
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'virtual box' in query :
            codePath= "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile (codePath)

        elif 'hello matrix' in query:
            speak ("hello sir how may i help you")

        elif 'saurav kon hai' in query :
            speak ("saurav is a gandu aadmi")    

        elif 'wish me' in query:
            speak ("good afternoon sir")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'jarvis favourite line' in query :
            speak ("The difference between your dream and reality is called commitment")

        elif 'aman bro' in query :
            speak ("yes sir, he is your room mate")    

        elif 'email to prince' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "princeiit423@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend faiz bhai. I am not able to send this email")    
