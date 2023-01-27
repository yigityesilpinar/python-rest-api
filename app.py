import os
from flask import Flask
from flask_smorest import Api
from resources.venue import blp as VenueBlueprint
from resources.item import blp as ItemBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint
from flask_jwt_extended import JWTManager

from db import db
import models


def create_app(db_url=None, jwt_secret_key=None):
    app = Flask(__name__)

    # Swagger
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Venues API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Database
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
    db.init_app(app)

    # JWT
    app.config["JWT_SECRET_KEY"] = jwt_secret_key or os.getenv(
        "JWT_SECRET_KEY", "165190795513706400064441539426923149524"
    )
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(VenueBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    return app
