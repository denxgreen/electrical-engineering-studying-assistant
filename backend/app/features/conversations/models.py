from datetime import datetime, UTC
import uuid

from sqlalchemy import Boolean, DateTime, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Conversation(Base):
    __tablename__ = 'conversations'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('students.user_id', ondelete='CASCADE'))

    student = relationship('Student', back_populates='conversations')
    messages = relationship('Message', back_populates='conversation')


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(UTC))
    ai_generated: Mapped[bool] = mapped_column(Boolean, default=False) 
    conversation_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('conversations.id', ondelete='CASCADE'))

    conversation = relationship('Conversation', back_populates='messages') 
