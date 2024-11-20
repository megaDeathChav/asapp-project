import json
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models.llmgemini import query_gemini_for_info

#models to represent the input format
class ConversationMessage(BaseModel):
    speaker: str
    text: str
    
# Represents the entire structure of the request body
# it expects a list of conversation messagge objects
class SingleConversationRequest(BaseModel):
    conversations: List[ConversationMessage]

class MultiConversationRequest(BaseModel):
    conversations: List[SingleConversationRequest]

app = FastAPI()

@app.post("/extract-info/")
async def extract_information(conversation_request: MultiConversationRequest):
    try:
        conversations_list = conversation_request.conversations

        all_extracted_info = []

        for conversation_data in conversations_list:
            formatted_conversation = [(msg.speaker, msg.text) for msg in conversation_data.conversations]
            extracted_info = query_gemini_for_info(formatted_conversation)
            all_extracted_info.append(extracted_info)

        return {"results": all_extracted_info}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#bert endpoints - tester
class ConversationMessage(BaseModel):
    speaker: str
    text: str

class MultiConversationRequest(BaseModel):
    conversations: List[List[ConversationMessage]]


app = FastAPI()

@app.post("/extract-info/")
async def extract_information(conversation_request: MultiConversationRequest):
    try:
        all_extracted_info = []

        # each convo
        for conversation_data in conversation_request.conversations:
            formatted_conversation = [(msg.speaker, msg.text) for msg in conversation_data]
            extracted_entities = extract_entities_from_conversation(formatted_conversation)
            all_extracted_info.append(extracted_entities)
        return {"results": all_extracted_info}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

