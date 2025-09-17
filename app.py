from fastapi import FastAPI, Request
from nlp_model import get_ai_response

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    ai_reply = get_ai_response(user_message)
    return {"reply": ai_reply}
