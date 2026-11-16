from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_session
from features.teachers import service


def get_teacher_service(session: Annotated[Session, Depends(get_session)]) -> service.TeacherService:
    return service.TeacherService(session) 


TeacherService = Annotated[service.TeacherService, Depends(get_teacher_service)]
