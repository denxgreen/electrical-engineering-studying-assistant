import uuid

from pydantic import BaseModel, ConfigDict

from schemas.user import UserBase


class StudentBase(UserBase):
    year_of_study: int


class StudentCreate(StudentBase):
    model_config = ConfigDict(from_attributes=True)
    
    password: str


class StudentResponse(StudentBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
