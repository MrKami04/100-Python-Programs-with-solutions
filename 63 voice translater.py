# voice translator using python 

# pip install googletrans : " https://pypi.org/project/googletrans/"
import googletrans
# print(googletrans.LANGUAGES)

print("😍 ------------------------- 😍") 
# text translator

print("😍 ------------------------- 😍") 
# voice translator
#pip install SpeechRecognition  :  "https://pypi.org/project/SpeechRecognition/"
# pip install PyAudio:  " https://pypi.org/project/PyAudio/"
import speech_recognition
recognizer = speech_recognition.Recognizer()

input_lang ="ur"
output_lang = "en" 
with speech_recognition.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language=input_lang)
    print(text)
    
translater = googletrans.Translator()
trans = translater.translate(text,dest=output_lang)
print(trans.text)


# pip install gTTS  : "https://pypi.org/project/gTTS/ "
import gtts

convert_audio = gtts.gTTS(trans.text, lang=output_lang)
convert_audio.save("hello.mp3")

# pip install playsound :  "   https://pypi.org/project/playsound/"

import playsound
playsound.playsound("hello.mp3")

