#this file is to connect bert to the API
import re
from typing import List, Dict

def extract_email(text: str) -> List[str]:
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def extract_phone(text: str) -> List[str]:
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(phone_pattern, text)

def extract_name(text: str) -> List[str]:
    # Placeholder for BERT NER or use regex for names if desired
    return []

def extract_entities_from_conversation(conversation: List[List[str]]) -> Dict[str, List[str]]:
    entities = {
        'email': set(),
        'phone': set(),
        'name': set()
    }
    text = ' '.join(message for _, message in conversation)
    entities['email'].update(extract_email(text))
    entities['phone'].update(extract_phone(text))
    entities['name'].update(extract_name(text))
    return {k: list(v) for k, v in entities.items()}
