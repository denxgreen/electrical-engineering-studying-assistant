import uuid

from pydantic import BaseModel, ConfigDict

from schemas.user import UserBase


class TeacherBase(UserBase):
    title: str


class TeacherCreate(TeacherBase):
    model_config = ConfigDict(from_attributes=True)
    
    password: str


class TeacherResponse(TeacherBase):
    model_config = ConfigDict(from_attributes=True)

    user_id: uuid.UUID
