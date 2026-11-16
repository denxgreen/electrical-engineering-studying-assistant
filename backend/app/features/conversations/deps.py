from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_session
from features.conversations import service


def get_conversation_service(session: Annotated[Session, Depends(get_session)]) -> service.ConversationService:
    return service.ConversationService(session)


ConversationService = Annotated[service.ConversationService, Depends(get_conversation_service)]
