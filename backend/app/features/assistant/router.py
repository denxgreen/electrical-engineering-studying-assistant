from typing import Annotated

from fastapi import APIRouter, Depends
import requests

from core.config import settings
from features.assistant.deps import get_assistant_service
from features.assistant.schemas import PromptRequest, PromptResponse
from features.assistant.service import AssistantService

router = APIRouter(
    prefix='/assistant',
    tags=['assistant']
)

url = 'https://api.groq.com/openai/v1/models'
headers = {
    'Authorization': f'Bearer {settings.groq_api_key}',
    'Content-Type': 'application/json'
}


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
