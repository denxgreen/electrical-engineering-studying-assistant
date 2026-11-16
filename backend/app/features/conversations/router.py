from typing import Annotated

from fastapi import APIRouter, HTTPException, status

from features.auth.deps import CurrentUser
from features.conversations.deps import ConversationService
from features.conversations.schemas import ConversationCreate, ConversationResponse
from features.users.models import UserRole

router = APIRouter(
    prefix='/conversations',
    tags=['conversations']
)


@router.get('/')
def get_conversations(
        current_user: CurrentUser,
        service: ConversationService
) -> list[ConversationResponse]:
    if current_user.role is not UserRole.ADMIN and current_user.role is not UserRole.TEACHER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list conversations",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    conversations = service.get_conversations()

    return conversations


@router.post('/')
def create_conversation(
        schema: ConversationCreate,
        current_user: CurrentUser,
        service: ConversationService 
) -> ConversationResponse:
    if current_user.role is not UserRole.ADMIN and current_user.role is not UserRole.STUDENT:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to create conversations",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    conversation = service.create_conversation(current_user.id)

    return conversation
