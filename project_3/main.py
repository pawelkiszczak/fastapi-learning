from fastapi import FastAPI

from .database import engine
from .models import Base
from .routers import admin, auth, todos, user

# Create an app instance
app = FastAPI()


# Healthcheck
@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


# Add routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)

# Bind database engine
Base.metadata.create_all(bind=engine)
