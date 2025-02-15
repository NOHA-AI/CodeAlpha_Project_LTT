# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/117M242orcDpT5SSWRVr__zZUydNKtNQ-
"""

# Install required libraries
!pip install nltk
!pip install spacy
!python -m spacy download en_core_web_sm

import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk

# Ensure all necessary data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Add this to resolve missing files


# Load SpaCy's language model
nlp = spacy.load("en_core_web_sm")

# Predefined FAQs
faqs = {
    "What is chlorophyll?": "Chlorophyll is a natural pigment found in plants that helps in photosynthesis. It's known for its health benefits like detoxification and boosting energy levels.",
    "How do I use chlorophyll products?": "You can add liquid chlorophyll to water or smoothies or take it as capsules, following the dosage on the product label.",
    "Are there side effects of using chlorophyll?": "Chlorophyll is generally safe, but excessive use might cause minor digestive discomfort. Consult a healthcare provider if you're unsure.",
    "Can chlorophyll help with detoxification?": "Yes, chlorophyll is known for its detoxifying properties and may help cleanse your system of toxins.",
    "How do I contact support?": "You can contact support via email at support@example.com.",
    "What is the pricing model?": "Our pricing model for chlorophyll products starts at $15 for liquid chlorophyll and $20 for capsules.",
    "Where can I find documentation?": "You can find product documentation and usage guidelines at docs.example.com.",
    "How do I reset my password?": "To reset your password, click 'Forgot Password' on the login page.",
    "Hello": "Hello! How can I assist you today?",
    "How can I help you?": "Feel free to ask about our products, services, or anything else you'd like to know!",
}

# Preprocess questions (convert to lowercase and tokenize)
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return tokens

# Find the best match for user input
def find_answer(user_input):
    user_tokens = set(preprocess(user_input))
    best_match = None
    max_overlap = 0

    for question in faqs:
        question_tokens = set(preprocess(question))
        overlap = len(user_tokens & question_tokens)  # Find common words
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = question

    if best_match:
        return faqs[best_match]
    else:
        return "Sorry, I don't have an answer for that. Please contact support for more help."

# Chatbot loop
def chatbot():
    print("Welcome to the FAQ Chatbot!")
    print("Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = find_answer(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()