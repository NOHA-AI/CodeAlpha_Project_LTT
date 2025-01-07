# TASK1
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
Special thanks to the developers of the `translate` library for making language translation accessible in Python.c

# TASK2
# FAQ Chatbot

This repository contains a simple Frequently Asked Questions (FAQ) Chatbot implemented in Python. The chatbot uses Natural Language Processing (NLP) techniques to understand user queries and provide relevant answers from a predefined list of FAQs.

## Features

- **Natural Language Understanding**: Utilizes SpaCy for language processing.
- **Tokenization and Stopword Removal**: Processes user input to filter out irrelevant information.
- **Interactive Chat**: Users can engage in a conversation, asking questions, and receiving responses until they choose to exit.
- **Simple FAQ Structure**: Answers common questions about chlorophyll and related topics.

## Requirements

Make sure you have Python 3.x installed on your machine. The following libraries are required:

- spacy
- nltk

You can install the required libraries using pip:

```bash
pip install spacy nltk
```

Additionally, you will need to download SpaCy's English language model. You can do this by running:

```bash
python -m spacy download en_core_web_sm
```

## Setup

Before running the chatbot, ensure you have downloaded the necessary components from the NLTK library:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

To run the chatbot, simply execute the following command in your terminal:

```bash
python chatbot.py
```

You will be greeted with a welcome message and can begin typing your questions. Enter `exit` to close the chatbot.

## Sample Interaction

```
Welcome to the FAQ Chatbot!
Type 'exit' to end the chat.

You: What is chlorophyll?
Chatbot: Chlorophyll is a natural pigment found in plants that helps in photosynthesis. It's known for its health benefits like detoxification and boosting energy levels.

You: How do I contact support?
Chatbot: You can contact support via email at support@example.com.

You: exit
Chatbot: Goodbye!
```

## Contributions

Contributions to improve the functionality or add features to the chatbot are welcome. Please fork the repository and submit a pull request.

## Acknowledgments

- [SpaCy](https://spacy.io/) for advanced NLP capabilities.
- [NLTK](https://www.nltk.org/) for general NLP tasks and utilities.

# TASK3 

# Annotated Video Processing with YOLO

This repository contains a Python script to perform object detection on a video using the YOLO (You Only Look Once) model. The script downloads a sample video from a given URL, processes each frame for object detection, annotates the frames, and finally combines the frames back into a video. The annotated video is displayed in a web-like environment (such as Google Colab).

## Features

- **Object Detection**: Utilizes the YOLOv8 model for real-time object detection.
- **Frame Processing**: Extracts frames from the video, performs detection, and saves annotated frames.
- **Video Reconstruction**: Combines the processed frames into an output video.
- **Video Display**: Allows for displaying the final annotated video within a web interface (e.g., Colab).

## Requirements

You will need the following to run this script:

- Python 3.x
- The `ultralytics` library for YOLOv8
- OpenCV for video processing
- FFmpeg for video handling (installed via command)

You can install the necessary libraries using:

```bash
pip install numpy opencv-python ultralytics
```

## Setup and Installation

This script is intended for use in environments that support the execution of shell commands, such as Google Colab. Here are the steps to set it up quickly:

1. **Clone the repository** or copy the script to your local environment or a Colab notebook.
  
2. **Install FFmpeg** (if not already installed in Colab):

   ```python
   !apt-get install -y ffmpeg
   ```

3. **Run the Code**: Execute the script. It includes downloading a sample video, processing each frame using the YOLO model, and combining the frames back into an annotated video. 

## Code Explanation

### Step-by-Step Breakdown

1. **Video Download**: The script downloads a sample video file from a specified URL and saves it to a temporary location.

2. **Model Initialization**: It loads the YOLOv8 model for object detection.

3. **Frame Processing**: Each frame of the video is read, processed, and annotated using the detection model. Annotated frames are saved in a temporary directory.

4. **Video Reconstruction**: After processing the frames, it combines them using FFmpeg to create the final annotated video.

5. **Display**: Finally, the annotated video is displayed in a web-based format.

### Usage Example

Here's how the interaction might look when using this script in a Google Colab environment:

```python
# Imports and installations
!apt-get install -y ffmpeg
!pip install ultralytics opencv-python

# Execute the video processing script (the above script) to see results
```

## Final Output

The final output is an annotated video, which will display the processed frames with object detection results. The video can be directly viewed in the Colab environment once processed.( it's uploaded to this repository)

## Contributions

Contributions to enhance functionality or improve performance are welcome. Please fork this repository and submit a pull request.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- [YOLO](https://github.com/ultralytics/yolov5) for object detection capabilities.
- [OpenCV](https://opencv.org/) for video processing functionality.
- [FFmpeg](https://ffmpeg.org/) for video manipulation tasks.


