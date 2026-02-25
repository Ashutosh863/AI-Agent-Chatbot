from fastapi import FastAPI
from schemas import ChatRequest , ChatResponse
from agent import run_agent

app = FastAPI()

@app.post("/chat",response_model=ChatResponse)
def chat(req:ChatRequest):
    response = run_agent(req.session_id,req.message)
    return ChatResponse(response=response)
    