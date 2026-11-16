from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from features.auth.deps import CurrentUser
from features.users.deps import UserService
from features.users.models import UserRole
from features.users.schemas import UserCreate, UserResponse

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def get_users(
        current_user: CurrentUser,
        service: UserService
) -> list[UserResponse]:
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list users",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    users = service.get_users()

    return users


@router.get('/me')
def get_current_user(current_user: CurrentUser) -> UserResponse:
    return current_user


@router.post('/')
def create_user(
        schema: UserCreate,
        current_user: CurrentUser,
        service: UserService        
) -> UserResponse:
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to create users",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    user = service.create_user(email=schema.email, password=schema.password)

    return user
