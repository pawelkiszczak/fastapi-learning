import models
from database import engine
from fastapi import FastAPI
from routers import admin, auth, todos, user

# Create an app instance
app = FastAPI()

# Add routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)

# Bind database engine
models.Base.metadata.create_all(bind=engine)
