from flask import Flask, request
from uuid import uuid4

venues = []

app = Flask(__name__)


@app.get("/venues")
def get_user_venues():
    return venues


@app.get("/venue/<string:id>")
def get_user_venue_by_id(id: str):
    for venue in venues:
        print(f"Checking venue id: {venue['id']}")
        print(f"for id: {id}")
        if str(venue["id"]) == id:
            return venue

    return {}, 404


@app.post("/venue")
def create_venue():
    post_data = request.get_json()
    if post_data:
        new_venue = {"id": uuid4(), "name": post_data["name"], "items": []}
        venues.append(new_venue)
        return new_venue, 201

    return {}
