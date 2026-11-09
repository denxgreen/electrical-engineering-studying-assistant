from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import requests

from core.config import settings
from database.db import get_session
from engines.groq import GroqEngine
from schemas.assistant import PromptRequest, PromptResponse
from services.assistant import AssistantService

router = APIRouter(
    prefix='/assistant',
    tags=['assistant']
)

url = 'https://api.groq.com/openai/v1/models'
headers = {
    'Authorization': f'Bearer {settings.groq_api_key}',
    'Content-Type': 'application/json'
}


def get_assistant_service(session: Annotated[Session, Depends(get_session)]) -> AssistantService:
    engine = GroqEngine(api_key=settings.groq_api_key, model='openai/gpt-oss-120b', system_prompt='Keep your response relatively concise. No styles of text.') 

    return AssistantService(engine=engine, session=session)


@router.get('/models')
def get_models() -> list[dict]:
    response = requests.get(url, headers=headers)
    
    print(type(response))

    return response.json().get('data')


@router.post('/generate')
def generate(
        prompt: PromptRequest, 
        service: Annotated[AssistantService, Depends(get_assistant_service)]
) -> PromptResponse:
    content = service.generate(prompt.content)
    return PromptResponse(content=content)
