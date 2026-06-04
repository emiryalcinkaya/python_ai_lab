"""
Chatbot V1 - Rule Based Chatbot

A simple chatbot built with Python.
Uses predefined rules to respond to user messages.
"""

def chatbot():

    # Ask the user for their name
    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}!")
    
    # Track the number of exchanged messages
    message_count = 0

    # Welcome message shown when the chatbot starts
    print("Bot: Hello! Type 'bye' to exit.")

    # Keep the chatbot running until the user exits
    while True:

        # Get user input and convert it to lowercase
        user_input = input("You: ").lower()
        message_count += 1

        # Check if the message contains a greeting
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi!")

        # Check if the user asks how the bot is doing
        elif "how are you" in user_input:
            print("Bot: I'm doing well!")

        # Check if the user says thanks
        elif "thanks" in user_input:
            print("Bot: You're welcome!")

        # Exit the chatbot when the user says bye
        elif "bye" in user_input:
            print(f"Bot: Goodbye {name}! We exchanged {message_count} messages.")
            break
        
        # Default response for unknown messages
        else:
            print("Bot: I don't understand.")

# Start the chatbot
chatbot()