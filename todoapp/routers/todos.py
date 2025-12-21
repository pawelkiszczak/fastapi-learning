from typing import Annotated, Any, Generator

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from ..database import SessionLocal
from ..models import Todo
from ..request_schemas import TodoRequest
from .auth import get_current_user

router = APIRouter(tags=["todo"])


# Get database connection
def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency injections
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]
USER_DEPENDENCY = Annotated[dict, Depends(get_current_user)]


# Endpoints
@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )
    return db.query(Todo).filter(Todo.owner_id == user.get("id")).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(
    user: USER_DEPENDENCY, db: DB_DEPENDENCY, todo_id: int = Path(gt=0)
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    todo_model = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
        .first()
    )
    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(
    user: USER_DEPENDENCY, db: DB_DEPENDENCY, todo_request: TodoRequest
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    todo_model = Todo(**todo_request.model_dump(), owner_id=user.get("id"))
    db.add(todo_model)
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    todo_request: TodoRequest,
    todo_id: int = Path(gt=0),
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    todo_model = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )

    for k, v in todo_request:
        setattr(todo_model, k, v)

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    user: USER_DEPENDENCY, db: DB_DEPENDENCY, todo_id: int = Path(gt=0)
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    todo_model = (
        db.query(Todo)
        .filter(Todo.id == todo_id)
        .filter(Todo.owner_id == user.get("id"))
        .first()
    )

    if todo_model is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Todo not found")

    db.delete(todo_model)
    db.commit()
