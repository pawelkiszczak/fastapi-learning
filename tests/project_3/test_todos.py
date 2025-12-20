from typing import Any, Generator

from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from project_3.database import Base
from project_3.main import app
from project_3.routers.todos import get_current_user, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


# Get override for database connection
def override_get_db() -> Generator[Session, Any, None]:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {"username": "pawkistest", "id": 1, "role": "admin"}


# Override dependencies when testing
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


def test_read_all_authenticated():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []