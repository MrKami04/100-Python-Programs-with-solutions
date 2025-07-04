import PyPDF2
from gtts import gTTS

# Open and read PDF
file = open('Introduction.pdf', mode='rb')
pdf_reader = PyPDF2.PdfReader(file)
pages = len(pdf_reader.pages)

# Extract all text from the PDF
full_text = ""
for i in range(0, pages):
    page = pdf_reader.pages[i]
    text = page.extract_text()
    if text:
        full_text += text

# Convert text to speech and save as MP3
tts = gTTS(text=full_text, lang='en')
tts.save("audiobook.mp3")

print("Audio saved as audiobook.mp3")
