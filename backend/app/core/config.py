from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / '.env',
        env_file_encoding='utf-8',
    )

    uvicorn_host: str
    uvicorn_port: int = 8000 

    groq_api_key: str 

    database_url: str

    secret_key: SecretStr
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 30
    

settings = Settings()
