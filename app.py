from fastapi import FastAPI, Request
from transformers import pipeline

# Load a conversational pipeline (can be changed to a custom model)
nlp = pipeline("conversational", model="microsoft/DialoGPT-medium")

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    # Generate AI response using NLP model
    conversation = nlp(user_message)
    ai_reply = conversation[0]['generated_text']
    return {"reply": ai_reply}
