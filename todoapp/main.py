from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

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


# Mount static files
app.mount("/static", StaticFiles(directory="todoapp/static"), name="static")


@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)
