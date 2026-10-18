import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from core.config import UVICORN_HOST, UVICORN_PORT
from routers import assistant

app = FastAPI()
app.include_router(assistant.router)

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
    uvicorn.run('main:app', host=UVICORN_HOST, port=int(UVICORN_PORT), reload=True)
