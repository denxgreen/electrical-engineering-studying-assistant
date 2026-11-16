from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_session
from features.users import service


def get_user_service(session: Annotated[Session, Depends(get_session)]) -> service.UserService:
    return service.UserService(session) 


UserService = Annotated[service.UserService, Depends(get_user_service)]
