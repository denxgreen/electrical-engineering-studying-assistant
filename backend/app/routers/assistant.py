from fastapi import APIRouter, Depends
import requests

from core.config import GROQ_API_KEY
from engines.groq import GroqEngine
from schemas.assistant import PromptRequest, PromptResponse
from services.assistant import AssistantService

router = APIRouter(
    prefix='/assistant',
    tags=['assistant']
)

url = 'https://api.groq.com/openai/v1/models'
headers = {
    'Authorization': f'Bearer {GROQ_API_KEY}',
    'Content-Type': 'application/json'
}

def get_assistant_service() -> AssistantService:
    return AssistantService(GroqEngine(api_key=GROQ_API_KEY, model='openai/gpt-oss-120b', system_prompt='Keep your response relatively concise. No lines, no styles of text.'))

@router.get('/models')
def get_models() -> list[dict]:
    response = requests.get(url, headers=headers)
    
    print(type(response))

    return response.json().get('data')

@router.post('/prompt')
def generate(
        prompt: PromptRequest, 
        model: str,
        service: AssistantService = Depends(get_assistant_service)
) -> PromptResponse:
    content = service.generate(prompt.content)
    return PromptResponse(content=content)
