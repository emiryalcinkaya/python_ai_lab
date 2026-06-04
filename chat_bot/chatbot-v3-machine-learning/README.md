# Chatbot V3 - Machine Learning Chatbot

A Machine Learning-powered chatbot built with Python and Scikit-Learn.

This project is the third step in my AI learning journey. Unlike previous versions that relied on manually written rules, this chatbot uses a Machine Learning model to predict user intents and generate responses.

## Project Evolution

### V1 - Rule Based Chatbot
User Message → Response

### V2 - Intent Detection Chatbot
User Message → Intent Detection → Response

### V3 - Machine Learning Chatbot
User Message → Machine Learning Model → Predicted Intent → Response

## Features

- User name recognition
- Message counter
- Machine Learning intent prediction
- Greeting, Status, Thanks, and Goodbye intents
- Random greeting responses
- Modular chatbot architecture

## Technologies Used

- Python
- Scikit-Learn
- CountVectorizer
- Multinomial Naive Bayes
- Random Module

## How It Works

### Training Data

hello       → greeting 
hi          → greeting 
hey         → greeting  

thanks      → thanks 
thank you   → thanks  

bye         → goodbye 
goodbye     → goodbye 

### Feature Extraction

Machine Learning models cannot understand raw text directly.

hello 

becomes something like:

text [1, 0, 0, 0] 

using:

python CountVectorizer() 

### Model Training

python model.fit(X, training_labels) 

The model learns relationships between words and intents.

### Prediction

hi bot       
↓ 
Greeting Intent       
↓ 
Hello! 

## Machine Learning Concepts Learned

- Training Data
- Labels
- Feature Extraction
- Text Vectorization
- CountVectorizer
- Naive Bayes Classification
- Model Training
- Prediction

## Example Session

Bot: What's your name? 
You: Emir  
Bot: Nice to meet you, Emir! 
Bot: Hello! Type 'bye' to exit.  
You: hi bot 
Bot: Hello!  
You: thank you 
Bot: You're welcome!  
You: bye 
Bot: Goodbye Emir! We exchanged 3 messages. 

## Author

Emir Yalçınkaya