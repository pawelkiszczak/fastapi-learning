from typing import Annotated

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from models import Todo
from sqlalchemy.orm import Session

# Create an app instance
app = FastAPI()

# Create models
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database settings
db_dependency = Annotated[Session, Depends(get_db)]


# Endpoints
@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todo).all()
