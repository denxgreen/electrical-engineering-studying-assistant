from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from core.security import verify_access_token
from features.auth import service
from features.users.deps import UserService
from features.users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def get_auth_service(users: UserService) -> service.AuthService:
    return service.AuthService(users)


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        users: UserService
) -> User | None:
    user_id = verify_access_token(token)

    if user_id is None:
        return None
    
    user = users.get_user_by_id(user_id)

    if not user:
        return None

    return user


AuthService = Annotated[service.AuthService, Depends(get_auth_service)]

CurrentUser = Annotated[User, Depends(get_current_user)]
