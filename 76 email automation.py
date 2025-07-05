# pip install secure-smtplib :    " https://pypi.org/project/secure-smtplib/"

import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3
# import
listenser = sr.Recognizer()
tts = pyttsx3.init()
def talking(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print("program is listening...")
        voice = listenser.listen(source)
        data = listenser.recognize_google(voice)
        print((data))
        return data.lower()
    
# for multiply user sand mail
dict = {"name":"receiver email"}

def send_mail(receiver, Subject, body ):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sender email","app password( if any issue then paste in gpt , tell you next process)")
    email = EmailMessage()
    email["From"] = "sender email"
    email["To"] = receiver
    email["Subject"] = Subject
    email.set_content(body)
    server.send_message(email)
    

def main_poc():
    talking("to whom do you want to send this email?")
    name = mic()
    receiver = dict[name]
    talking("speak the subject of the email")
    Subject = mic()
    talking("speak the message of the email")
    body = mic()
    send_mail(receiver, Subject, body)
    print("Your email ha been sent!!")
main_poc()
