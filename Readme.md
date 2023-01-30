# A simple rest API with flask

## Prerequisites

If you haven't done yet, create a virtual env

```
python3.11 -m venv .venv
```

## Dependencies

Update requirements.txt

```
pip3 freeze > requirements.txt 
```

## Static type checking

```
mypy app.py 
```

## Docker

Build a local docker image

```
 docker build -t python-rest-api .
```

Run a local container

```
docker run -p 5000:5000 --name container-python-rest-api python-rest-api:latest
```

Run dev containers with docker-compose

```
docker-compose up
```


## Migrations

setup initial migrations

```
flask db init
```

generate migration files

```
flask db migrate
```

apply migration

```
flask db upgrade
```

## DotEnv File

You will need to create and file a '.env' file. Here are sample values:

```
MAILGUN_API_KEY=
MAILGUN_DOMAIN=
REDIS_PASSWORD=VfpFtOFGxx0BRYJ6WH5IZNEWBzcuZtJ9
TASK_QUEUE_REDIS_URL=redis://:VfpFtOFGxx0BRYJ6WH5IZNEWBzcuZtJ9@redis-queue:6379
USE_BACKGROUND_WORKER=true
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=POSTGRES_DB
DATABASE_URL=postgresql://POSTGRES_USER:POSTGRES_PASSWORD@db:5432/POSTGRES_DB
```

