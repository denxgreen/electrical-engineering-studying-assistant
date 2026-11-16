from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from features.auth.deps import AuthService
from features.auth.schemas import Token

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/login')
def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        service: AuthService
) -> Token:
    access_token = service.login(form_data.username, form_data.password)

    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return Token(access_token=access_token, token_type='bearer')
