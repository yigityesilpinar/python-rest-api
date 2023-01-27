from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schemas import ItemSchema, UpdateItemSchema
from models import ItemModel
from db import db


blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<int:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @blp.arguments(UpdateItemSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_update, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_update["price"]
            item.name = item_update["name"]
        else:
            item = ItemModel(id=item_id, **item_update)
        db.session.add(item)
        db.session.commit()
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted!"}


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured on insert item")
        return item
