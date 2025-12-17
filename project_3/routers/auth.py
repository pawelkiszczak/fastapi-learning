from typing import Annotated, Any, Generator

from database import SessionLocal
from fastapi import APIRouter, Depends
from models import User
from passlib.context import CryptContext
from request_schemas import CreateUserRequest
from sqlalchemy.orm import Session
from starlette import status

# Declare router
router = APIRouter()

# Declare hashing algo and context
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Get database connection
def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database settings
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: DB_DEPENDENCY,
    create_user_request: CreateUserRequest,
):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()
