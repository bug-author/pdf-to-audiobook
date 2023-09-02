import pdfplumber
from gtts import gTTS

def pdf_to_text(pdf_path):
    pdf_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text()
    return pdf_text

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    extracted_text = pdf_to_text(pdf_path)
    
    if extracted_text:
        tts = gTTS(text=extracted_text, lang='en')
        tts.save("sample_audiobook.mp3")
