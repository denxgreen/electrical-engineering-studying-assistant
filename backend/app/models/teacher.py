import uuid

from sqlalchemy import UUID, Enum, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.user import UserRole


class Teacher(Base):
    __tablename__ = 'teachers'
    __table_args__ = (
        CheckConstraint('user_role = \'TEACHER\'', name='ck_teachers_role'),
        ForeignKeyConstraint(['user_id', 'user_role'], ['users.id', 'users.role'], ondelete='CASCADE', name='fk_teachers_id_role')
    )

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.TEACHER)
    title: Mapped[str]

    user = relationship('User', back_populates='teacher_profile')
    
    @property
    def email(self) -> str:
        return self.user.email
