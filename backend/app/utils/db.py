from database.db import engine
import models


def create_tables():
    models.Base.metadata.create_all(bind=engine)
