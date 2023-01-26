from uuid import uuid4
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import venues


blp = Blueprint("venues", __name__, description="Operations on venues")


@blp.route("/venue/<string:venue_id>")
class Venue(MethodView):
    def get(self, venue_id):
        if venue_id not in venues:
            abort(404, message="Venue not found")
        else:
            return venues[venue_id]

    def delete(self, venue_id):
        if venue_id not in venues:
            abort(404, message="Venue not found")
        else:
            del venues[venue_id]
            return {"message": f"Venue id: {venue_id} is deleted"}


@blp.route("/venue")
class VenueList(MethodView):
    def get(self):
        return venues

    def post(self):
        post_data = request.get_json()
        if post_data:
            new_venue_id_uuid = uuid4()
            new_venue = {
                "id": new_venue_id_uuid,
                "name": post_data["name"],
                "items": [],
            }
            venues[str(new_venue_id_uuid)] = new_venue
            return new_venue, 201

        return {}
