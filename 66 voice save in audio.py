import PyPDF2
import pyttsx3

file = open('Introduction.pdf', mode='rb')
pdf_reader = PyPDF2.PdfReader(file)
pages = len(pdf_reader.pages)

full_text = ""
for i in range(0, pages):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    if text:
        full_text += text

# Save audio as WAV
melo = pyttsx3.init()
melo.save_to_file(full_text, 'audiobook.wav')
melo.runAndWait()

print("Audio saved as audiobook.wav")
