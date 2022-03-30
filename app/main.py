from fastapi import FastAPI
from .routers import post, user, root, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# Line used to generate the database based on defined models.
# Commented because we are using "alembic".
# models.Base.metadata.create_all(bind=engine)

title = "Blog FastAPI"
description = f"""
{title} helps you do awesome stuff. 🚀

## Blogs

You will be able to:

* **Create blogs**.
* **Read all blogs**.
* **Delete own blogs**.
* **Vote blogs**.

## Users

You will be able to:

* **Create users**.
* **Login users**.
"""

app = FastAPI(
    title=title,
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Robert Gherlan",
        "url": "https://www.linkedin.com/in/robert-gherlan/",
        "email": "robertgherlan@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root.router)
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
