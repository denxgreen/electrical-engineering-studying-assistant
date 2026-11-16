import uuid

from sqlalchemy import Enum, CheckConstraint, ForeignKeyConstraint, UUID, column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from features.users.models import UserRole


class Teacher(Base):
    __tablename__ = 'teachers'
    __table_args__ = (
        CheckConstraint(
            column('user_role', Enum(UserRole)) == UserRole.TEACHER,
            name='ck_teachers_role'
        ),
        ForeignKeyConstraint(['user_id', 'user_role'], ['users.id', 'users.role'], ondelete='CASCADE', name='fk_teachers_id_role')
    )

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    user_role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.TEACHER)
    title: Mapped[str]

    user = relationship('User', back_populates='teacher_profile')
    
    @property
    def email(self) -> str:
        return self.user.email
