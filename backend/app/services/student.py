from sqlalchemy import select
from sqlalchemy.orm import Session

from models.student import Student
from models.user import UserRole
from services.user import UserService


class StudentService(UserService):
    def __init__(self, session: Session):
        super().__init__(session)

    def get_students(self) -> list[Student]:
        result = self._session.execute(select(Student))

        students = result.scalars().all()  

        return list(students)

    def create_student(self, email: str, password: str, year_of_study: int) -> Student:
        user = super().create_user(email, password, UserRole.STUDENT)
        
        student = Student(year_of_study=year_of_study, user=user)

        self._session.add(student)
        self._session.commit()
        self._session.refresh(student)

        return student 
