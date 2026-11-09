import uuid

from sqlalchemy import UUID, Enum, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.user import UserRole


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        CheckConstraint('user_role = \'STUDENT\'', name='ck_students_role'),
        ForeignKeyConstraint(['user_id', 'user_role'], ['users.id', 'users.role'], ondelete='CASCADE', name='fk_students_id_role')
    )

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.STUDENT)
    year_of_study: Mapped[int]

    user = relationship('User', back_populates='student_profile')
    conversations = relationship('Conversation', back_populates='student')

    @property
    def email(self) -> str:
        return self.user.email
