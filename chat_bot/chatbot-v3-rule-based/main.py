"""
Chatbot V3 - Machine Learning Chatbot

This chatbot uses a Machine Learning model
to predict user intents.
"""

import random

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# Training data
training_sentences = [
    "hello",
    "hi",
    "hey",
    "good morning",

    "how are you",
    "how is it going",
    "how are things",

    "thanks",
    "thank you",

    "bye",
    "goodbye",
    "see you"
]

# Intent labels
training_labels = [
    "greeting",
    "greeting",
    "greeting",
    "greeting",

    "status",
    "status",
    "status",

    "thanks",
    "thanks",

    "goodbye",
    "goodbye",
    "goodbye"
]


# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_sentences)

# Train the model
model = MultinomialNB()
model.fit(X, training_labels)


def detect_intent(user_input):
    """
    Predict the user's intent using the trained model.
    """

    # Convert user message into a vector
    user_vector = vectorizer.transform([user_input])

    # Predict the intent
    prediction = model.predict(user_vector)

    return prediction[0]


def chatbot():

    # Ask the user for their name
    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}!")

    # Track exchanged messages
    message_count = 0

    # Greeting responses
    greeting_responses = [
        "Hi!",
        "Hello!",
        "Nice to see you!",
        "Hey there!"
    ]

    print("Bot: Hello! Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower()
        message_count += 1

        # Predict intent using ML model
        intent = detect_intent(user_input)

        if intent == "greeting":
            print("Bot:", random.choice(greeting_responses))

        elif intent == "status":
            print("Bot: I'm doing well!")

        elif intent == "thanks":
            print("Bot: You're welcome!")

        elif intent == "goodbye":
            print(
                f"Bot: Goodbye {name}! "
                f"We exchanged {message_count} messages."
            )
            break

        else:
            print("Bot: I don't understand.")


# Start chatbot
chatbot()