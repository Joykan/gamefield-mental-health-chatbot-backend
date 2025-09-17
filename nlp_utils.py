from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sentiment")

def detect_mental_health(message):
    result = classifier(message)
    # Basic example: look for negative sentiment
    if result[0]['label'] == 'NEGATIVE':
        return "It sounds like you're going through a tough time. Would you like to talk more or get some help?"
    return None
