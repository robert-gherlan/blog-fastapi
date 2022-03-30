import pytest

from app.database import get_db
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    # run our code before running the test
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    # run the code after our test finishes
