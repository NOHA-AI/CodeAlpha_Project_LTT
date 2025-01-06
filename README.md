# CodeAlpha_Project_Language_Translation_Tool

## Overview
This is a simple **Language Translation Tool** developed as part of my internship with CodeAlpha. The tool allows users to translate text from one language to another using pre-trained translation models. It demonstrates the use of Python's `translate` library for quick and easy text translation.

## Features
- Translate text between multiple languages.
- Supports popular languages like English, Spanish, French, German, Chinese, Hindi, Arabic, and Russian.
- Interactive user input for source and destination languages.

## How It Works
1. The user inputs the text they want to translate.
2. The user specifies the source and destination language codes (e.g., `en` for English, `es` for Spanish).
3. The tool uses the `Translator` class from the `translate` library to perform the translation.

## Requirements
- Python 3.x
- `translate` library

## Installation
1. Clone this repository or download the files:
   ```bash
   git clone https://github.com/YourGitHubUsername/CodeAlpha_Project_Language_Translation_Tool.git

2.Install the required library:
 ```bash
pip install translate

3.Run the script:
 ```bash
python language_translation_tool.py

## Installation
-Run the tool.
-Enter the text you want to translate.
-Provide the source language code (e.g., en for English).
-Provide the destination language code (e.g., es for Spanish).
-View the translated text.

Example
 ```bash
Language Codes Reference:
English (en), Spanish (es), French (fr), German (de), Chinese (zh), Hindi (hi), Arabic (ar), Russian (ru)

Enter the text you want to translate: Hello, how are you?
Enter the source language code (e.g., 'en' for English): en
Enter the destination language code (e.g., 'es' for Spanish): es

Translated Text:
Hola, ¿cómo estás?

## Limitations
The tool uses a local library and may not support advanced translation models like Google Translate API.
Requires an active internet connection for translations.
## Future Improvements
Integrate with APIs like Google Translate or Microsoft Translator for enhanced translation accuracy.
Add a graphical user interface (GUI) for ease of use.
Support batch translation for large texts or files.

## Author
This project was developed by Nouhaila KORCHI as part of the CodeAlpha Internship Program.
