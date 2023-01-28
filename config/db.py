import os
from flask import Flask
from flask_migrate import Migrate
from db import db


def configure_db(app: Flask, db_url):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
