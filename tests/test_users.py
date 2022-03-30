import pytest
from jose import jwt

from app import schemas
from fastapi import status

from app.config import settings
from tests.fixtures.token import VALID_USER_NAME, VALID_USER_PASSWORD


def test_create_user(client):
    response = client.post("/v1/users/",
                           json=schemas.UserCreate(email="test1@example.com", password="test123456").dict())
    assert response.status_code == status.HTTP_201_CREATED

    new_user = schemas.User(**response.json())
    assert new_user.email == "test1@example.com"
    assert new_user.id > 0
    assert new_user.created_at is not None


def test_login(test_user, client):
    response = client.post("/v1/login/", data={"username": VALID_USER_NAME, "password": VALID_USER_PASSWORD})
    assert response.status_code == status.HTTP_200_OK
    token = schemas.Token(**response.json())
    assert token.access_token is not None
    assert token.token_type == "bearer"

    payload = jwt.decode(token.access_token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    assert int(payload.get("user_id")) > 0


@pytest.mark.parametrize("username, password, status_code", [
    (VALID_USER_NAME, "wrong_password", 403),
    ("wrong_username", VALID_USER_PASSWORD, 403),
    ("wrong_username", "wrong_password", 403),
    (None, VALID_USER_PASSWORD, 422),
    (VALID_USER_NAME, None, 422)
])
def test_incorrect_login(test_user, client, username, password, status_code):
    response = client.post("/v1/login/", data={"username": username, "password": password})
    assert response.status_code == status_code
