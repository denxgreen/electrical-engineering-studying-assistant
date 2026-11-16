from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from db.base import Base

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session


def create_tables():
    Base.metadata.create_all(bind=engine)
