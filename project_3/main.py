from typing import Annotated, Any, Generator

import models
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Path
from models import Todo
from request_schemas import TodoRequest
from sqlalchemy.orm import Session
from starlette import status

# Create an app instance
app = FastAPI()

# Create models
models.Base.metadata.create_all(bind=engine)


# Get database connection
def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database settings
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


# Endpoints
@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: DB_DEPENDENCY):
    return db.query(Todo).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: DB_DEPENDENCY, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is not None:
        return todo_model

    raise HTTPException(404, detail="Todo not found")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: DB_DEPENDENCY, todo_request: TodoRequest):
    todo_model = Todo(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()


@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: DB_DEPENDENCY, todo_request: TodoRequest, todo_id: int = Path(gt=0)
):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    for k, v in todo_request:
        setattr(todo_model, k, v)

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: DB_DEPENDENCY, todo_id: int = Path(gt=0)):
    # todo_model = db.query(Todo).filter(Todo.id==todo_id).first()
    todo_model = db.get(Todo, todo_id)
    if todo_model is None:
        raise HTTPException(404, detail="Todo not found")

    db.delete(todo_model)
    db.commit()
