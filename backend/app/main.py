from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import settings
from db.session import create_tables
from features.assistant.router import router as assistant_router
from features.auth.router import router as auth_router
from features.conversations.router import router as conversations_router
from features.students.router import router as students_router
from features.teachers.router import router as teachers_router
from features.users.router import router as users_router
import db.registry

create_tables()

app = FastAPI()

app.include_router(assistant_router)
app.include_router(auth_router)
app.include_router(conversations_router)
app.include_router(students_router)
app.include_router(teachers_router)
app.include_router(users_router)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.uvicorn_host, port=settings.uvicorn_port, reload=True)
