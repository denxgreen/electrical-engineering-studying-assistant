from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_session
from schemas.student import StudentCreate, StudentResponse
from services.student import StudentService

router = APIRouter(
    prefix='/students',
    tags=['students']
)


def get_student_service(session: Annotated[Session, Depends(get_session)]) -> StudentService:
    return StudentService(session) 


@router.get('/')
def get_students(service: Annotated[StudentService, Depends(get_student_service)]) -> list[StudentResponse]:
    students = service.get_students()

    return students

@router.post('/')
def create_student(
        schema: StudentCreate,
        service: Annotated[StudentService, Depends(get_student_service)]
        
) -> StudentResponse:
    student = service.create_student(email=schema.email, password=schema.password, year_of_study=schema.year_of_study)

    return student
