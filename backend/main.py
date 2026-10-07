import os

from dotenv import load_dotenv
import uvicorn

load_dotenv()

UVICORN_HOST = os.getenv('UVICORN_HOST')
UVICORN_PORT = os.getenv('UVICORN_PORT')

if __name__ == '__main__':
    uvicorn.run('app.app:app', host=UVICORN_HOST, port=int(UVICORN_PORT), reload=True)
