from fastapi import FastAPI

app = FastAPI()

@app.get('/')
@app.get('/index')
async def index() -> str:
    return 'Hello, there!'
