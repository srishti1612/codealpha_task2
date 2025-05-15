import nltk
import random
import string

from nltk.chat.util import Chat, reflections

# Download NLTK data files (run once)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing fine. What about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No worries!", "Don't worry about it!"]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you. Just tell me your problem."]
    ],
    [
        r"(.*) your name ?",
        ["I'm a simple chatbot. You can call me Bot!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Interesting... tell me more."]
    ]
]

# Create and start the chatbot
def chatbot():
    print("Hi! I'm your basic chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
