# Chatbot V5 - RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot powered by Llama 3 and Ollama.

This project is the fifth step in my AI learning journey. Unlike the previous version that relied only on a Large Language Model, this chatbot first searches a knowledge base and then uses the retrieved information to generate more accurate and context-aware responses.

## Project Evolution

### V1 - Rule Based Chatbot
User Message → Response

### V2 - Intent Detection Chatbot
User Message → Intent Detection → Response

### V3 - Machine Learning Chatbot
User Message → ML Model → Intent Prediction → Response

### V4 - LLM Chatbot
User Message → Llama 3 → Generated Response

### V5 - RAG Chatbot
User Message → Knowledge Base Search → Llama 3 → Generated Response

## Features

- Llama 3 integration through Ollama
- Local knowledge base support
- Context retrieval system
- Retrieval-Augmented Generation (RAG)
- Interactive terminal chat
- Local AI model execution
- Context-aware responses

## Technologies Used

- Python
- Ollama
- Llama 3
- Text Processing
- Lists & Dictionaries
- Loops
- Functions

## How It Works

User Message  
↓  
Knowledge Base Search  
↓  
Relevant Context Retrieval  
↓  
Llama 3  
↓  
Generated Response

The chatbot searches a local knowledge base for relevant information before generating a response. The retrieved context is sent to the language model, allowing the chatbot to answer questions using external knowledge rather than relying only on the model's internal knowledge.

## Example Session

You: What does RAG mean?  
Bot: RAG stands for Retrieval-Augmented Generation. It allows a chatbot to retrieve relevant information from a knowledge base before generating a response.

You: What is Ollama?  
Bot: Ollama is a platform that allows users to run large language models locally on their own computer.

## Learning Goals

- Retrieval-Augmented Generation (RAG)
- Knowledge Base Design
- Information Retrieval
- Context Injection
- LLM Integration
- AI Application Development

## Future Improvements

- Vector Database Integration
- Embeddings
- ChromaDB
- PDF Knowledge Bases
- Semantic Search
- Advanced RAG Pipelines

## Author

Emir Yalçınkaya