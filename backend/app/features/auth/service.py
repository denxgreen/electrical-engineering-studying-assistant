from core.security import create_access_token, verify_password
from features.users.models import User
from features.users.service import UserService


class AuthService:
    def __init__(self, users: UserService):
        self._users = users

    def authenticate(self, email: str, password: str) -> User | None:
        user = self._users.get_user_by_email(email)

        if not user or not verify_password(password, user.password_hash):
            return None

        print('Point')

        return user
        
    def login(self, email: str, password: str) -> str | None:
        user = self.authenticate(email, password)
    
        if not user:
            return None

        access_token = create_access_token({'sub': str(user.id)})

        return access_token 

