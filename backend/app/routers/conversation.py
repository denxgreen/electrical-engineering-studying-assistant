from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_session 
from schemas.conversation import ConversationCreate, ConversationRead
from services.conversation import ConversationService

router = APIRouter(
    prefix='/conversation',
    tags=['conversation']
)


def get_conversation_service(session: Annotated[Session, Depends(get_session)]) -> ConversationService:
    return ConversationService(session)


@router.get('/')
def get_conversations(service: Annotated[ConversationService, Depends(get_conversation_service)]) -> list[ConversationRead]:
    conversations = service.get_conversations()

    return conversations

@router.post('/')
def create_conversation(
        schema: ConversationCreate,
        service: Annotated[ConversationService, Depends(get_conversation_service)]
) -> ConversationRead:
    conversation = service.create_conversation(schema.student_id)

    return conversation
