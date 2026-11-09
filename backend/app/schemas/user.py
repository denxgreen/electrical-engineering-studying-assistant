import uuid

from pydantic import BaseModel, ConfigDict, EmailStr

from models.user import UserRole


class UserBase(BaseModel):
    email: EmailStr
    

class UserCreate(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    password: str


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    role: UserRole
