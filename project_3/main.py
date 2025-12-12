import models
from database import engine
from fastapi import FastAPI
from routers import auth, todos

# Create an app instance
app = FastAPI()

# Add routers
app.include_router(auth.router)
app.include_router(todos.router)

# Bind database engine
models.Base.metadata.create_all(bind=engine)
