import re
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Define a set of patterns and responses
patterns = {
    r'hi|hello|hey': [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
    ],
    r'how are you': [
        "I'm just a bot, but I'm doing fine. Thanks!",
        "All systems go!",
    ],
    r'what is your name': [
        "I'm ChatBot, your virtual assistant.",
        "You can call me ChatBot.",
    ],
    r'(.*) your name': [
        "My name is ChatBot. What's yours?",
    ],
    r'(.*) help (.*)': [
        "Sure, I'm here to help. What do you need?",
        "Tell me more about how I can assist.",
    ],
    r'(.*) weather (.*)': [
        "Sorry, I can't provide weather updates now.",
    ],
    r'(.*) (location|city)': [
        "I'm just a bot, I exist in the cloud!",
    ],
    r'bye|exit|quit': [
        "Goodbye! Have a nice day.",
        "Bye! Talk to you later.",
    ],
    r'(.*)': [
        "I didn't understand that. Can you rephrase?",
        "Interesting... can you tell me more?",
        "I'm not sure I understand. Can you elaborate?",
    ]
}

# Function to match user input to patterns
def match_pattern(user_input):
    user_input = user_input.lower()
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "I'm not sure how to respond to that."

# Main chatbot loop
def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("ChatBot: Goodbye! 👋")
            break
        response = match_pattern(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
