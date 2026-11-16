from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_session
from features.students import service


def get_student_service(session: Annotated[Session, Depends(get_session)]) -> service.StudentService:
    return service.StudentService(session) 


StudentService = Annotated[service.StudentService, Depends(get_student_service)]
