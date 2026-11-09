from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core.auth import create_access_token, verify_password
from routers.users import get_user_service
from schemas.auth import Token
from services.user import UserService


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/token')
def token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        service: Annotated[UserService, Depends(get_user_service)]
) -> Token:
    user = service.get_user_by_email(form_data.username) 
    
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    pass

    access_token = create_access_token(data={'sub': str(user.id)}) 
    
    return Token(access_token=access_token, token_type='bearer')
