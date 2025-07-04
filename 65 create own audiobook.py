# pip install pyttsx3  :  " https://pypi.org/project/pyttsx3/"
# pip install PyPDF2  : "  https://pypi.org/project/PyPDF2/"

import pyttsx3
import PyPDF2
file = open('Introduction.pdf', mode='rb')

pdf_reader = PyPDF2.PdfReader(file)
pages = len(pdf_reader.pages)
print(pages)
melo = pyttsx3.init()
for i in range(0, pages):
    page =pdf_reader.pages[i]
    text=page.extract_text()
    melo.say(text)
    melo.runAndWait()
