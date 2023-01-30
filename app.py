from flask import Flask
from config.jwt import configure_jwt
from config.swagger import configure_swagger
from config.api import configure_api
from config.db import configure_db
from config.task_queue import configure_task_queue
from config.features import is_background_worker_enabled
from dotenv import load_dotenv


def create_app(db_url=None, jwt_secret_key=None, task_queue_url=None):
    app = Flask(__name__)
    load_dotenv()

    if is_background_worker_enabled():
        configure_task_queue(app=app, task_queue_url=task_queue_url)
    configure_swagger(app)
    configure_db(app=app, db_url=db_url)
    configure_jwt(app=app, jwt_secret_key=jwt_secret_key)
    configure_api(app)
    return app
