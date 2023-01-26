# A simple rest API with flask

## Prerequisites

If you haven't done yet, create a virtual env

```
python3.11 -m venv .venv
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

Run dev mode in docker

```
docker run -p 5000:5000 -w /app -v "$(pwd):/app" --name container-python-rest-api python-rest-api:latest
```

or using the dev bash script

```
./dev
```
