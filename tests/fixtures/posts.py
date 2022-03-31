import pytest

from app import models


@pytest.fixture
def test_posts(test_user, second_test_user, session):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user["id"]
    }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user["id"]
    }, {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user["id"]
    }, {
        "title": "4th title",
        "content": "4th content",
        "owner_id": second_test_user["id"]
    }]
    posts = list(map(create_post_model, posts_data))
    session.add_all(posts)
    session.commit()

    return session.query(models.Post).all()


def create_post_model(data):
    return models.Post(**data)
