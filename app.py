from flask import Flask, request
from flask_smorest import abort
from uuid import uuid4

venues = {}
items = {}

app = Flask(__name__)


@app.get("/venues")
def get_user_venues():
    return venues


@app.get("/venue/<string:id>")
def get_user_venue_by_id(id: str):
    if id not in venues:
        abort(404, message="Venue not found")
    else:
        return venues[id]


@app.post("/venue")
def create_venue():
    post_data = request.get_json()
    if post_data:
        new_venue_id_uuid = uuid4()
        new_venue = {"id": new_venue_id_uuid, "name": post_data["name"], "items": []}
        venues[str(new_venue_id_uuid)] = new_venue
        return new_venue, 201

    return {}
