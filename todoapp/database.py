import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(override=True)

SQLITE_DB_NAME = os.getenv("SQLITE_DB_NAME")
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{SQLITE_DB_NAME}"

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
