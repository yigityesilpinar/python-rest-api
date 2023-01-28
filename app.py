from flask import Flask
from config.jwt import configure_jwt
from config.swagger import configure_swagger
from config.api import configure_api
from config.db import configure_db


def create_app(db_url=None, jwt_secret_key=None):
    app = Flask(__name__)
    configure_swagger(app)
    configure_db(app=app, db_url=db_url)
    configure_jwt(app=app, jwt_secret_key=jwt_secret_key)
    configure_api(app)
    return app
