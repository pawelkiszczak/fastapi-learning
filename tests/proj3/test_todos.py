from fastapi import status

from project_3.models import Todo
from project_3.routers.todos import get_current_user, get_db
from tests.utils import (
    TestingSessionLocal,
    app,
    client,
    override_get_current_user,
    override_get_db,
    test_todo,
)

# Override dependencies when testing
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "complete": False,
            "title": "Learn to code",
            "description": "Do so every day",
            "id": 1,
            "priority": 5,
            "owner_id": 1,
        }
    ]


def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "complete": False,
        "title": "Learn to code",
        "description": "Do so every day",
        "id": 1,
        "priority": 5,
        "owner_id": 1,
    }


def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


def test_create_todo(test_todo):
    request_data = {
        "title": "New Todo!",
        "description": "New todo description",
        "priority": 3,
        "complete": False,
    }

    response = client.post("/todo/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 2).first()
    assert model.title == request_data.get("title")
    assert model.description == request_data.get("description")
    assert model.complete == request_data.get("complete")
    assert model.priority == request_data.get("priority")


def test_update_todo(test_todo):
    request_data = {
        "title": "Change the title",
        "description": "Need to learn more",
        "priority": 1,
        "complete": True,
    }

    response = client.put("/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model.title == request_data.get("title")
    assert model.description == request_data.get("description")
    assert model.complete == request_data.get("complete")
    assert model.priority == request_data.get("priority")


def test_update_todo_not_found(test_todo):
    request_data = {
        "title": "Change the title",
        "description": "Need to learn more",
        "priority": 1,
        "complete": True,
    }

    response = client.put("/todo/999", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}


def test_delete_todo(test_todo):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model is None


def test_delete_todo_not_found():
    response = client.delete("/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
