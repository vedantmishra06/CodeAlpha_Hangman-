import nltk
from nltk.stem import WordNetLemmatizer
import random
import json

# Sample intents (this could be loaded from a JSON file for scalability)
intents = {
    "intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "Hello", "Hey", "Good day", "What's up"],
         "responses": ["Hello!", "Hi there!", "Hey!", "Hi, how can I help you?"]},

        {"tag": "goodbye",
         "patterns": ["Bye", "See you", "Goodbye", "I am leaving"],
         "responses": ["Goodbye!", "See you soon!", "Bye! Take care!"]},

        {"tag": "thanks",
         "patterns": ["Thanks", "Thank you", "Appreciate it"],
         "responses": ["You're welcome!", "No problem!", "Glad I could help!"]},

        {"tag": "name",
         "patterns": ["What's your name?", "Who are you?"],
         "responses": ["I'm a chatbot!", "I'm your friendly assistant chatbot."]},

        {"tag": "noanswer",
         "patterns": [],
         "responses": ["Sorry, I don't understand.", "Can you rephrase that?"]}
    ]
}

lemmatizer = WordNetLemmatizer()

def tokenize_and_lemmatize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in tokens]

def classify(sentence):
    sentence_words = tokenize_and_lemmatize(sentence)
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = tokenize_and_lemmatize(pattern)
            if any(word in sentence_words for word in pattern_words):
                return intent
    return {"tag": "noanswer", "responses": intents["intents"][-1]["responses"]}

def chatbot():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        intent = classify(user_input)
        response = random.choice(intent["responses"])
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
