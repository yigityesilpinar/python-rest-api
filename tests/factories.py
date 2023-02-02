from models.user import UserModel
from db import db
from pythonrestapi.application import application


def create_user(email: str, password: str):
    user = UserModel(email=email, password=password)
    with application.app_context():
        db.session.add(user)
        db.session.commit()
    return user
