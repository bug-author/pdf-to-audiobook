import pdfplumber
from pydub import AudioSegment
import subprocess
import os

def pdf_to_text(pdf_path, start_page, end_page):
    pdf_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(start_page, end_page + 1):
            page = pdf.pages[page_num]
            pdf_text += page.extract_text()
    return pdf_text

def text_to_audio_mac(text, output_path="output.aiff"):
    subprocess.run(["say", "-o", output_path, text])

def merge_audio_files(audio_files, output_file):
    combined = AudioSegment.empty()
    for file in audio_files:
        audio = AudioSegment.from_file(file, format="aiff")
        combined += audio
    combined.export(output_file, format="mp3")

if __name__ == "__main__":
    pdf_path = "large_sample.pdf"
    total_pages = len(pdfplumber.open(pdf_path).pages)
    chunk_size = 10
    audio_files = []
    
    for i in range(0, total_pages, chunk_size):
        start_page = i
        end_page = min(i + chunk_size - 1, total_pages - 1)
        extracted_text = pdf_to_text(pdf_path, start_page, end_page)
        
        if extracted_text:
            audio_output_path = f"output_{start_page}_{end_page}.aiff"
            text_to_audio_mac(extracted_text, output_path=audio_output_path)
            audio_files.append(audio_output_path)
    
    merge_audio_files(audio_files, "large_sample_audiobook.mp3")
    for audio_file in audio_files:
        os.remove(audio_file)
