# pdf-to-audiobook
### PDF to Audiobook Converter in Python

## Introduction

This project provides a comprehensive Python script to convert PDFs into audiobooks. The script is tailored for handling both small and large PDF files, making it versatile for a variety of use-cases.

## Legal Disclaimer

This tool is intended for educational purposes and personal use only. Make sure to only convert those PDFs that you have the legal rights to. Unauthorized copying or distribution of copyrighted material is illegal and may result in legal repercussions.

## Features

- Text extraction from PDFs.
- Text-to-speech conversion.
- Supports Google Text-to-Speech (gTTS) for smaller PDFs.
- Utilizes macOS's built-in Text-to-Speech engine for larger PDFs.
- Audio file merging for larger PDFs to create a seamless audiobook.

## Dependencies

This project uses a number of Python libraries which you can install via `pip`:

```bash
pip install pdfplumber
pip install gtts
pip install pydub
```

## How to Use

### For Smaller PDFs

1. Replace `"sample.pdf"` in the code with the path of your own PDF file.
2. Run the script.
3. An audiobook file `sample_audiobook.mp3` will be generated.

```bash
python3 smaller_pdf_to_audiobook.py
```

### For Larger PDFs

1. Replace `"sample.pdf"` in the code with the path of your own PDF file.
2. Run the script.
3. Individual audio files will be created for each chunk of pages, which will then be merged into `sample_audiobook.mp3`.

```bash
python3 larger_pdf_to_audiobook.py
```

## Algorithm Explanation

### Smaller PDFs

1. **Text Extraction with `pdfplumber`**: The whole PDF is processed at once to extract text.
2. **Text-to-Speech with `gTTS`**: The extracted text is converted into a single MP3 file.

### Larger PDFs

1. **Text Extraction with `pdfplumber`**: Text is extracted in chunks to facilitate better memory management and API usage.
2. **Text-to-Speech with macOS's `say` command**: Each text chunk is converted into an individual audio file.
3. **Audio File Merging with `pydub`**: All audio chunks are merged into a single audiobook.

## Contribution

Feel free to fork the project and make your own changes or suggest any improvements via pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
