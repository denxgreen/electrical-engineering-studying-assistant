from datetime import datetime
import uuid

from pydantic import BaseModel, ConfigDict, Field


class MessageBase(BaseModel):
    content: str = Field(min_length=1) 
    created_at: datetime 
    ai_generated: bool


class MessageCreate(MessageBase):
    model_config = ConfigDict(from_attributes=True)

    conversation_id: uuid.UUID


class MessageRead(MessageBase):
    model_config = ConfigDict(from_attributes=True)

    conversation_id: uuid.UUID
