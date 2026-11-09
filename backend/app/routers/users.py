from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.auth import oauth2_scheme, verify_access_token
from database.db import get_session
from schemas.user import UserCreate, UserResponse
from services.user import UserService 

router = APIRouter(
    prefix='/users',
    tags=['users']
)


def get_user_service(session: Annotated[Session, Depends(get_session)]) -> UserService:
    return UserService(session) 


@router.get('/')
def get_users(service: Annotated[UserService, Depends(get_user_service)]) -> list[UserResponse]:
    users = service.get_users()

    return users

@router.get('/me')
def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    service: Annotated[UserService, Depends(get_user_service)]
) -> UserResponse:
    user_id = verify_access_token(token)

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid or expired token',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    user = service.get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return user

@router.post('/')
def create_user(
        schema: UserCreate,
        service: Annotated[UserService, Depends(get_user_service)]
        
) -> UserResponse:
    user = service.create_user(email=schema.email, password=schema.password)

    return user
