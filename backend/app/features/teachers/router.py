from fastapi import APIRouter, HTTPException, status

from features.auth.deps import CurrentUser
from features.teachers.deps import TeacherService
from features.teachers.schemas import TeacherCreate, TeacherResponse
from features.users.models import UserRole

router = APIRouter(
    prefix='/teachers',
    tags=['teachers']
)


@router.get('/')
def get_teachers(
        current_user: CurrentUser,
        service: TeacherService
) -> list[TeacherResponse]:
    if current_user.role is not UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list students",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    teachers = service.get_teachers()

    return teachers


@router.post('/')
def create_teacher(
        schema: TeacherCreate,
        current_user: CurrentUser,
        service: TeacherService
) -> TeacherResponse:
    if current_user.role is not UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list students",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    teacher = service.create_teacher(email=schema.email, password=schema.password, title=schema.title)

    return teacher
