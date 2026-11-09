import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Conversation(Base):
    __tablename__ = 'conversations'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('students.user_id', ondelete='CASCADE'))

    student = relationship('Student', back_populates='conversations')
    messages = relationship('Message', back_populates='conversation')
