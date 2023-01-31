from flask import Flask
from pythonrestapi.jwt import configure_jwt
from pythonrestapi.swagger import configure_swagger
from pythonrestapi.api import configure_api
from pythonrestapi.db import configure_db
from pythonrestapi.task_queue import configure_task_queue
from pythonrestapi.features import is_background_worker_enabled
from pythonrestapi.config import Config


def create_app(name: str, config: Config) -> Flask:
    app = Flask(name)
    app.config.from_mapping(config)
    if is_background_worker_enabled():
        configure_task_queue(app=app)
    configure_swagger(app)
    configure_db(app=app)
    configure_jwt(app=app)
    configure_api(app)
    return app
