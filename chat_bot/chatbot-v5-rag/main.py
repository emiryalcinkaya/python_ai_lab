"""
Chatbot V5 - Simple RAG Chatbot with Ollama

This chatbot searches a local knowledge base first,
then sends the retrieved context to a local Llama model using Ollama.
"""

import ollama


def load_knowledge_base(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def retrieve_context(question, knowledge_base):
    sentences = knowledge_base.split("\n")

    matched_sentences = []

    for sentence in sentences:
        for word in question.lower().split():
            if word in sentence.lower():
                matched_sentences.append(sentence)
                break

    return "\n".join(matched_sentences)


knowledge_base = load_knowledge_base("knowledge_base.txt")

print("Bot: Hello! Ask me something. Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    context = retrieve_context(user_input, knowledge_base)

    prompt = f"""
Use the context below to answer the question.

If the context does not contain enough information, say that you do not know.

Context:
{context}

Question:
{user_input}

Answer:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Bot:", response["message"]["content"])