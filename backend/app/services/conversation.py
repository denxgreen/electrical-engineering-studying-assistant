import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.conversation import Conversation


class ConversationService:
    def __init__(self, session: Session):
        self._session = session


    def get_conversations(self) -> list[Conversation]:
        result = self._session.execute(select(Conversation))

        conversations = result.scalars().all()  

        return list(conversations)


    def create_conversation(self, student_id: uuid.UUID) -> Conversation:
        conversation = Conversation(student_id=student_id)
        
        self._session.add(conversation)
        self._session.commit()
        self._session.refresh(conversation)

        return conversation
