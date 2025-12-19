from typing import Annotated, Any, Generator

from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from models import User
from passlib.context import CryptContext
from request_schemas import UserVerification
from sqlalchemy.orm import Session
from starlette import status

from .auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])


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
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: USER_DEPENDENCY, db: DB_DEPENDENCY):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    return db.query(User).filter(User.id == user.get("id")).first()


@router.put("/password", status_code=status.HTTP_200_OK)
async def change_password(
    user: USER_DEPENDENCY,
    db: DB_DEPENDENCY,
    user_verification: UserVerification,
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    user_model = db.query(User).filter(User.id == user.get("id")).first()

    if not bcrypt_context.verify(
        user_verification.password, user_model.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Error on password change"
        )

    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()


@router.put("/phone", status_code=status.HTTP_200_OK)
async def change_phone_number(
    user: USER_DEPENDENCY, db: DB_DEPENDENCY, phone_number: str
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed"
        )

    user_model = db.query(User).filter(User.id == user.get("id")).first()
    user_model.phone_number = phone_number

    db.add(user_model)
    db.commit()
