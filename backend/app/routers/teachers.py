from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_session
from schemas.teacher import TeacherCreate, TeacherResponse
from services.teacher import TeacherService

router = APIRouter(
    prefix='/teachers',
    tags=['teachers']
)


def get_teacher_service(session: Annotated[Session, Depends(get_session)]) -> TeacherService:
    return TeacherService(session) 


@router.get('/')
def get_teachers(service: Annotated[TeacherService, Depends(get_teacher_service)]) -> list[TeacherResponse]:
    teachers = service.get_teachers()

    return teachers

@router.post('/')
def create_teacher(
        schema: TeacherCreate,
        service: Annotated[TeacherService, Depends(get_teacher_service)]
        
) -> TeacherResponse:
    teacher = service.create_teacher(email=schema.email, password=schema.password, title=schema.title)

    return teacher
