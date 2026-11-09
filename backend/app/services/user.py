import uuid

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from core.auth import hash_password
from models.user import User, UserRole
from models.student import Student
from models.teacher import Teacher


class UserService:
    def __init__(self, session: Session):
        self._session = session    

    def get_user_by_email(self, email: str) -> User | None:
        result = self._session.execute(select(User).where(func.lower(User.email) == func.lower(email)))

        user = result.scalars().first()

        return user

    def get_user_by_id(self, id: str) -> User | None:
        result = self._session.execute(select(User).where(User.id == id))

        user = result.scalars().first()

        return user

    def get_users(self) -> list[User]:
        result = self._session.execute(select(User))

        users = result.scalars().all()  

        return list(users)

    def create_user(self, email: str, password: str, role: UserRole = UserRole.ADMIN) -> User:
        user = User(email=email.lower(), password_hash=hash_password(password), role=role) 

        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)

        return user

