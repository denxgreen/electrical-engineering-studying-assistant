from fastapi import APIRouter, HTTPException, status

from features.auth.deps import CurrentUser
from features.students.deps import StudentService
from features.students.schemas import StudentCreate, StudentResponse
from features.users.models import UserRole

router = APIRouter(
    prefix='/students',
    tags=['students']
)


@router.get('/')
def get_students(
        current_user: CurrentUser,
        service: StudentService
) -> list[StudentResponse]:
    if current_user.role is not UserRole.ADMIN and current_user.role is not UserRole.TEACHER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list students",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    students = service.get_students()

    return students


@router.post('/')
def create_student(
        schema: StudentCreate,
        current_user: CurrentUser,
        service: StudentService
) -> StudentResponse:
    if current_user.role is not UserRole.ADMIN and current_user.role is not UserRole.TEACHER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to list students",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    student = service.create_student(email=schema.email, password=schema.password, year_of_study=schema.year_of_study)

    return student
