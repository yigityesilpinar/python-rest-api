from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schemas import TagSchema, TagAndItemSchema, PlainTagSchema
from models import TagModel, VenueModel, ItemModel
from db import db


blp = Blueprint("tags", __name__, description="Operations on tags")


@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @blp.response(
        202,
        description="Deletes a tag if not item is linked with it",
        example={"message": "Tag deleted."},
    )
    @blp.alt_response(
        404,
        description="Tag not found",
    )
    @blp.alt_response(
        400,
        description="Returned if the tag can not be deleted since its linked to items",
    )
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted."}
        else:
            abort(400, message="Tag can not be deleted since its linked to items")


@blp.route("/venue/<string:venue_id>/tag")
class TagsInVenue(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, venue_id):
        venue = VenueModel.query.get_or_404(venue_id)
        return venue.tags.all()

    @blp.arguments(PlainTagSchema)
    @blp.response(201, TagSchema)
    def post(self, tag_data, venue_id):
        tag = TagModel(**tag_data, venue_id=venue_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured on insert tag")
        return tag


@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagToItem(MethodView):
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        item = ItemModel.query.get_or_404(item_id)
        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured on linking a tag and an item")
        return tag

    @blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        item = ItemModel.query.get_or_404(item_id)
        if tag in item.tags:
            item.tags.remove(tag)
        else:
            abort(404, message="No links exists between the tag and item")
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured on unlinking a tag and an item")
        return {
            "message": "Item has removed from the tag",
            "tag": tag,
            "item": item,
        }
