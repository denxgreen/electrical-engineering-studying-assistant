from datetime import datetime, timedelta, UTC

from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
import jwt

from core.config import settings

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return password_hash.verify(password=password, hash=hash)


def create_access_token(
        data: dict, 
        expire_delta: timedelta = timedelta(settings.access_token_expire_minutes)
) -> str:
    to_encode = data.copy()
    expire_time = datetime.now(UTC) + expire_delta
    to_encode.update({'exp': expire_time})

    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=settings.secret_key.get_secret_value(),
        algorithm=settings.algorithm
    )

    return encoded_jwt


def verify_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(
           jwt=token,
           key=settings.secret_key.get_secret_value(),
           algorithms=[settings.algorithm],
           options={'require': ['exp', 'sub']},
        )
    except jwt.InvalidTokenError:
        return None
    else:
        return payload.get('sub')
