import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import settings
from utils.db import create_tables
import routers

create_tables()

app = FastAPI()
app.include_router(routers.assistant.router)
app.include_router(routers.auth.router)
app.include_router(routers.students.router)
app.include_router(routers.teachers.router)
app.include_router(routers.users.router)
#app.include_router(conversation.router)

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
