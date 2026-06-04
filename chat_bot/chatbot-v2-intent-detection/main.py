"""
Chatbot V2 - Intent Detection Chatbot

This chatbot detects user intents
and responds accordingly.
"""

import random

def detect_intent(user_input):
    """
    Detect the user's intent based on keywords.
    """

    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning"
    ]

    status_questions = [
        "how are you",
        "how are things",
        "how is it going"
    ]

    thanks = [
        "thanks",
        "thank you"
    ]

    goodbyes = [
        "bye",
        "goodbye",
        "see you"
    ]

    # Check greeting intent
    for word in greetings:
        if word in user_input:
            return "greeting"

    # Check status intent
    for word in status_questions:
        if word in user_input:
            return "status"

    # Check thanks intent
    for word in thanks:
        if word in user_input:
            return "thanks"

    # Check goodbye intent
    for word in goodbyes:
        if word in user_input:
            return "goodbye"

    # Return unknown if no intent matches
    return "unknown"

def chatbot():

    # Ask the user for their name
    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}!")

    # Track the number of exchanged messages
    message_count = 0

    # Different responses for greetings
    greeting_responses = [
        "Hi!",
        "Hello!",
        "Nice to see you!",
        "Hey there!"
    ]

    # Welcome message shown when the chatbot starts
    print("Bot: Hello! Type 'bye' to exit.")

    # Keep the chatbot running until the user exits
    while True:

        # Get user input and convert it to lowercase
        user_input = input("You: ").lower()

        # Increase message counter
        message_count += 1

        # Detect the user's intent
        intent = detect_intent(user_input)

        # Respond based on the detected intent
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

# Start the chatbot
chatbot()