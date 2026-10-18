import os

from dotenv import load_dotenv

load_dotenv()

UVICORN_HOST = os.getenv('UVICORN_HOST')
UVICORN_PORT = os.getenv('UVICORN_PORT')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
