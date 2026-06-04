"""
Chatbot V4 - LLM Chatbot

This chatbot uses Llama 3 through Ollama
to generate responses and remember
conversation history.
"""

import ollama


def chatbot():

    # Store conversation history
    history = []

    # Count exchanged messages
    message_count = 0

    print("Bot: Hello! Type 'bye' to exit.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "bye":
            print(
                f"Bot: Goodbye! "
                f"We exchanged {message_count} messages."
            )
            break

        # Save user message
        history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Send entire conversation history
        response = ollama.chat(
            model="llama3",
            messages=history
        )

        bot_response = response["message"]["content"]

        # Save bot response
        history.append(
            {
                "role": "assistant",
                "content": bot_response
            }
        )

        message_count += 1

        print("\nBot:")
        print(bot_response)
        print()


chatbot()