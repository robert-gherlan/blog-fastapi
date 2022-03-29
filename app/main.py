from fastapi import FastAPI
from .routers import post, user, root, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# Line used to generate the database based on defined models.
# Commented because we are using "alembic".
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
