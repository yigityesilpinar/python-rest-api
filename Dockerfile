FROM python:3.11.1

ENV PIP_NO_CACHE_DIR=true \
    PIP_DEFAULT_TIMEOUT=10 \
    POETRY_VERSION=1.3.2 \
    POETRY_HOME="/home/user/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN pip install poetry==${POETRY_VERSION}

ENV PATH="${POETRY_HOME}/bin:${PATH}"

RUN useradd -ms /bin/bash app-user

USER app-user

WORKDIR /app

COPY --chown=app-user pyproject.toml poetry.lock ./
RUN poetry lock --check
RUN poetry install --no-dev --no-root

COPY . .

CMD ["/bin/bash", "docker-entrypoint.sh"]