import os

from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI, Request, Form 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()

UVICORN_HOST = os.getenv('UVICORN_HOST')
UVICORN_PORT = os.getenv('UVICORN_PORT')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

client = Groq(api_key=GROQ_API_KEY)

app = FastAPI()

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

@app.post('/api/assistant/response')
async def get_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
            {
                'role': 'user',
                'content': prompt,
            }
        ],
    )

    response = response.choices[0].message.content
    
    return response

if __name__ == '__main__':
    uvicorn.run('main:app', host=UVICORN_HOST, port=int(UVICORN_PORT), reload=True)
