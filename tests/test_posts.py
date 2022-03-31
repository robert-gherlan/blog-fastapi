import pytest
from fastapi import status

from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/v1/posts")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(test_posts)

    def validate(post):
        return schemas.PostOut(**post)

    posts_map = map(validate, response.json())
    assert len(list(posts_map)) == len(test_posts)


def test_unauthorized_user_get_all_post(client):
    response = client.get("/v1/posts")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_unauthorized_user_get_one_post(client, test_posts):
    response = client.get(f"/v1/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_user_get_one_non_existing_post(authorized_client):
    response = authorized_client.get("/v1/posts/12345678")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_authorized_user_get_one_existing_post(authorized_client, test_posts):
    response = authorized_client.get(f"/v1/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_200_OK
    post = schemas.PostOut(**response.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content


@pytest.mark.parametrize("title, content, published", [
    ("title", "content", True),
    ("title 1", "content 1", False),
    ("title 2", "content 2", False)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    response = authorized_client.post("/v1/posts/",
                                      json=schemas.PostCreate(title=title, content=content, published=published).dict())
    assert response.status_code == status.HTTP_201_CREATED
    saved_post = schemas.Post(**response.json())
    assert saved_post.title == title
    assert saved_post.content == content
    assert saved_post.published == published
    assert saved_post.owner_id == test_user["id"]


def test_create_post_default_published(authorized_client, test_user, test_posts):
    title = "post title"
    content = "post content"
    response = authorized_client.post("/v1/posts/",
                                      json=schemas.PostCreate(title=title, content=content).dict())
    assert response.status_code == status.HTTP_201_CREATED
    saved_post = schemas.Post(**response.json())
    assert saved_post.title == title
    assert saved_post.content == content
    assert saved_post.published is True
    assert saved_post.owner_id == test_user["id"]


def test_unauthorized_create_post(client):
    response = client.post("/v1/posts/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_unauthorized_delete_post(client, test_posts):
    response = client.delete(f"/v1/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_delete_post(authorized_client, test_posts):
    response = authorized_client.delete(f"/v1/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_non_existing_post(authorized_client):
    response = authorized_client.delete("/v1/posts/12345678")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_others_user_post(authorized_client, test_user, test_posts):
    response = authorized_client.delete(f"/v1/posts/{test_posts[3].id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_update_post(authorized_client, test_user, test_posts):
    post = schemas.PostCreate(title="NEW TITLE", content="NEW CONTENT")
    response = authorized_client.put(f"/v1/posts/{test_posts[0].id}", json=post.dict())
    assert response.status_code == status.HTTP_200_OK
    updated_post = schemas.Post(**response.json())
    assert updated_post.title == post.title
    assert updated_post.content == post.content


def test_update_others_user_post(authorized_client, test_user, test_posts):
    post = schemas.PostCreate(title="NEW TITLE", content="NEW CONTENT")
    response = authorized_client.put(f"/v1/posts/{test_posts[3].id}", json=post.dict())
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_update_unauthorized_user(client, test_user, test_posts):
    post = schemas.PostCreate(title="NEW TITLE", content="NEW CONTENT")
    response = client.put(f"/v1/posts/{test_posts[3].id}", json=post.dict())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_update_non_existing_post(authorized_client, test_user, test_posts):
    post = schemas.PostCreate(title="NEW TITLE", content="NEW CONTENT")
    response = authorized_client.put(f"/v1/posts/1234567", json=post.dict())
    assert response.status_code == status.HTTP_404_NOT_FOUND
