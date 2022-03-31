import pytest

from app import schemas, models
from fastapi import status


@pytest.fixture
def test_vote(test_posts, session, test_user):
    new_vote = models.Vote(user_id=test_user["id"], post_id=test_posts[0].id)
    session.add(new_vote)
    session.commit()


def test_vote_on_post(authorized_client, test_posts):
    vote = schemas.Vote(post_id=test_posts[0].id, direction=1)
    response = authorized_client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_201_CREATED


def test_vote_twice_on_post(authorized_client, test_posts, test_vote):
    vote = schemas.Vote(post_id=test_posts[0].id, direction=1)
    response = authorized_client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_409_CONFLICT


def test_delete_vote(authorized_client, test_posts, test_vote):
    vote = schemas.Vote(post_id=test_posts[0].id, direction=0)
    response = authorized_client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_201_CREATED


def test_add_vote_on_non_existing_post(authorized_client, test_posts):
    vote = schemas.Vote(post_id="12345678", direction=1)
    response = authorized_client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_non_existing_vote(authorized_client, test_posts):
    vote = schemas.Vote(post_id=test_posts[3].id, direction=0)
    response = authorized_client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_vote_unauthenticated_on_post(client, test_posts):
    vote = schemas.Vote(post_id=test_posts[0].id, direction=1)
    response = client.post("/v1/vote/", json=vote.dict())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
