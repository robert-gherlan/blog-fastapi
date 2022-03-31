import pytest
from fastapi import status
from app import schemas
from app.oauth2 import create_access_token

VALID_USER_NAME = "test@example.com"
VALID_USER_NAME_1 = "test1@example.com"
VALID_USER_PASSWORD = "test1234"


@pytest.fixture
def test_user(client) -> schemas.UserCreate:
    user_data = schemas.UserCreate(email=VALID_USER_NAME, password=VALID_USER_PASSWORD)
    response = client.post("/v1/users/", json=user_data.dict())
    assert response.status_code == status.HTTP_201_CREATED
    new_user = response.json()
    new_user['password'] = user_data.password
    return new_user


@pytest.fixture
def second_test_user(client) -> schemas.UserCreate:
    user_data = schemas.UserCreate(email=VALID_USER_NAME_1, password=VALID_USER_PASSWORD)
    response = client.post("/v1/users/", json=user_data.dict())
    assert response.status_code == status.HTTP_201_CREATED
    new_user = response.json()
    new_user['password'] = user_data.password
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token(data={"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client
