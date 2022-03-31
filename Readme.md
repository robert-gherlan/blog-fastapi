# Blog FastAPI

This project uses: **Python**, **PostgreSQL**, **FastAPI**, **SQLAlchemy**, **Alembic** and **pytest**.

## PostgreSQL Install Steps
You can install PostgreSQL 14.2 on your computer following the steps from this [link](https://www.postgresql.org/download/).

Or you can install PostgreSQL with Docker using:
```shell script
docker pull postgres:14.2
```

## Installing application

To install the application use following commands:
```shell script
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment configuration

Following environment variables need to be set in your OS or added in a new **.env** file from root of this directory.
```
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_NAME = ADD_HERE_YOUR_DB_NAME
DATABASE_USERNAME = ADD_HERE_YOUR_DB_USERNAME
DATABASE_PASSWORD = ADD_HERE_YOUR_DB_PASSWORD
JWT_SECRET_KEY = ADD_HERE_A_JWT_SECRET_KEY
JWT_ALGORITHM = HSA256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60
```

You can generate a JWT secret key using following command:
```shell script
openssl rand -hex 32
```

## Install pytest

You can install **pytest** using:
```shell script
pip install -U pytest
```

## Run tests

You can run your tests using:
```shell script
pytest -s -v
```

## Running the application in dev mode

You can run your application in dev mode that enables live coding using:
```shell script
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Related Guides

- Python ([guide](https://www.python.org/docs/)): Python is a programming language that lets you work quickly and integrate systems more effectively.
- PostgreSQL ([guide](https://www.postgresql.org/docs/)): The World's Most Advanced Open Source Relational Database
- FastAPI ([guide](https://fastapi.tiangolo.com/)): FastAPI framework, high performance, easy to learn, fast to code, ready for production
- SQLAlchemy ([guide](https://www.sqlalchemy.org/)): SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- Alembic ([guide](https://alembic.sqlalchemy.org/en/latest/index.html)): Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.
- pytest ([guide](https://docs.pytest.org/en/7.1.x/contents.html)): Creating and executing Python tests.