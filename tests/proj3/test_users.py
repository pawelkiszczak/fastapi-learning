from fastapi import status

from project_3.routers.user import get_current_user, get_db
from tests.utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "januszeiro"
    assert response.json()["email"] == "januszeiro@test.pl"
    assert response.json()["first_name"] == "janusz"
    assert response.json()["last_name"] == "eiro"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "1233212310"


def test_change_password_success(test_user):
    response = client.put(
        "/user/password",
        json={"password": "testpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_200_OK


def test_change_password_invalid_current_password(test_user):
    response = client.put(
        "/user/password",
        json={"password": "wrongpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phone/3215235213")
    assert response.status_code == status.HTTP_204_NO_CONTENT
