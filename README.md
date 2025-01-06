# Language Translation Tool

## Overview
The Language Translation Tool is a simple Python application that allows users to translate text from one language to another. It uses the `translate` library to perform the translations and supports a variety of languages.

## Features
- User-friendly interface that provides a list of language codes.
- Ability to translate text between multiple languages.
- Error handling to manage any issues during the translation process.

## Language Codes Reference
The following language shortcuts are available for use:
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Chinese (zh)
- Hindi (hi)
- Arabic (ar)
- Russian (ru)

## Requirements
- Python 3.x
- `translate` library

### Installation
You can install the required library using pip. Run the following command in your terminal:

```bash
pip install translate
```

## Usage
1. Run the script using Python.
   
   ```bash
   python translate_tool.py
   ```

2. Follow the prompts to:
   - Enter the text you want to translate.
   - Input the source language code (e.g., 'en' for English).
   - Input the destination language code (e.g., 'es' for Spanish).

3. The translated text will be displayed in the console.

## Example
```bash
Enter the text you want to translate: Hello, how are you?
Enter the source language code (e.g., 'en' for English): en
Enter the destination language code (e.g., 'es' for Spanish): es

Translated Text:
Hola, ¿cómo estás?
```

## Error Handling
If an error occurs during the translation process (e.g., unsupported language code), a descriptive message will be displayed.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
Special thanks to the developers of the `translate` library for making language translation accessible in Python.



