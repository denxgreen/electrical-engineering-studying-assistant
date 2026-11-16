from core.config import settings
from features.assistant.engines.groq import GroqEngine
from features.assistant.service import AssistantService


def get_assistant_service() -> AssistantService:
    engine = GroqEngine(api_key=settings.groq_api_key, model='openai/gpt-oss-120b', system_prompt='Keep your response relatively concise. No styles of text.') 

    return AssistantService(engine)
