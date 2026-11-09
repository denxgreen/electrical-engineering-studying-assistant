import enum
import uuid

from sqlalchemy import UUID, String, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class UserRole(str, enum.Enum):
    ADMIN = 'ADMIN'
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'


class User(Base):
    __tablename__ = 'users' 
    __table_args__ = (
        UniqueConstraint('id', 'role', name='uq_users_id_role'),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    #password: Mapped[str]
    password_hash: Mapped[str]
    #password_hash: Mapped[]
    #first_name: Mapped[str]
    #last_name: Mapped[str]
    role: Mapped[UserRole] = mapped_column(Enum(UserRole))

    student_profile = relationship('Student', back_populates='user', uselist=False) 
    teacher_profile = relationship('Teacher', back_populates='user', uselist=False) 
