from sqlalchemy import select
from sqlalchemy.orm import Session

from models.teacher import Teacher
from models.user import UserRole
from services.user import UserService


class TeacherService(UserService):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_teachers(self) -> list[Teacher]:
        result = self._session.execute(select(Teacher))

        teachers = result.scalars().all()  

        return list(teachers)

    def create_teacher(self, email: str, password: str, title: str) -> Teacher:
        user = super().create_user(email, password, UserRole.TEACHER)
        
        teacher = Teacher(title=title, user=user)

        self._session.add(teacher)
        self._session.commit()
        self._session.refresh(teacher)

        return teacher 
