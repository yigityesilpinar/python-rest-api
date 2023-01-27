from uuid import uuid4
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import VenueSchema, UpdateVenueSchema
from sqlalchemy.exc import SQLAlchemyError
from models import VenueModel
from db import db


blp = Blueprint("venues", __name__, description="Operations on venues")


@blp.route("/venue/<string:venue_id>")
class Venue(MethodView):
    @blp.response(200, VenueSchema)
    def get(self, venue_id):
        venue = VenueModel.query.get_or_404(venue_id)
        return venue

    @blp.arguments(UpdateVenueSchema)
    @blp.response(200, VenueSchema)
    def put(self, venue_update, venue_id):
        venue = VenueModel.query.get(venue_id)
        if venue:
            venue.name = venue_update["name"]
        else:
            venue = VenueModel(id=venue_id, **venue_update)
        db.session.add(venue)
        db.session.commit()
        return venue

    def delete(self, venue_id):
        venue = VenueModel.query.get_or_404(venue_id)
        db.session.delete(venue)
        db.session.commit()
        return {"message": "Venue deleted!"}


@blp.route("/venue")
class VenueList(MethodView):
    @blp.response(200, VenueSchema(many=True))
    def get(self):
        return VenueModel.query.all()

    @blp.arguments(VenueSchema)
    @blp.response(201, VenueSchema)
    def post(self, venue_data):
        venue = VenueModel(**venue_data)
        try:
            db.session.add(venue)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured on instert venue")
        return venue
