import json
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from llmgemini import query_gemini_for_info 

# Define data models to represent the input format
class ConversationMessage(BaseModel):
    speaker: str
    text: str
    
# Represents the entire structure of the request body
# it expects a list of conversationmessagge objects
class ConversationRequest(BaseModel):
    conversation: List[ConversationMessage]


app = FastAPI()

@app.post("/extract-info/")
async def extract_information(conversation_request: ConversationRequest):
    try:
    
        conversation = conversation_request.conversation

    
        formatted_conversation = [(msg.speaker, msg.text) for msg in conversation]
        
        
        extracted_info = query_gemini_for_info(formatted_conversation)

    
        return {"extracted_info": extracted_info}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

