import os
from flask import Flask
from flask_migrate import Migrate
from db import db


def configure_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
