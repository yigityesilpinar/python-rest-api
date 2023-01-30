import requests
import os
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError
from schemas import UserSchema
from models import UserModel
from db import db
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    get_jwt_identity,
)
from config.blocklist import BLOCKLIST

blp = Blueprint("users", __name__, description="Operations on users")


def send_simple_message(to: str, subject: str, body: str):
    domain = os.getenv("MAILGUN_DOMAIN")
    api_key = os.getenv("MAILGUN_API_KEY")
    if not api_key:
        raise RuntimeError("MAILGUN_API_KEY must be provided")
    if not domain:
        raise RuntimeError("MAILGUN_DOMAIN must be provided")
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"<postmaster@{domain}>",
            "to": [to],
            "subject": subject,
            "text": body,
        },
    )


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        try:
            user = UserModel(
                email=user_data["email"],
                password=pbkdf2_sha256.hash(user_data["password"]),
            )
            db.session.add(user)
            db.session.commit()
            send_simple_message(
                to=user.email,
                subject="Succesfully signed up!",
                body="Welcome to our app!",
            )
        except IntegrityError:
            abort(409, message="email already exist")
        else:
            return {"message": "User created."}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.email == user_data["email"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            abort(401, message="Invalid credentials")


@blp.route("/refresh")
class UserRefreshToken(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        refreshed_access_token = create_access_token(user_id, fresh=False)
        new_refresh_token = create_refresh_token(identity=user_id)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {
            "access_token": refreshed_access_token,
            "refresh_token": new_refresh_token,
        }


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt().get("jti")
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out!"}


@blp.route("/user")
class User(MethodView):
    @blp.response(200, UserSchema)
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        return user

    @jwt_required(fresh=True)
    def delete(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted."}
