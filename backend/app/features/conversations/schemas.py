import uuid

from pydantic import BaseModel, ConfigDict


class ConversationBase(BaseModel):
    pass


class ConversationCreate(ConversationBase):
    model_config = ConfigDict(from_attributes=True)


class ConversationResponse(ConversationBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    student_id: uuid.UUID
