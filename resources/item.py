from uuid import uuid4
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items


blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        if item_id not in items:
            abort(404, message="Item not found")
        else:
            return items[item_id]

    def delete(self, item_id):
        if item_id not in items:
            abort(404, message="Item not found")
        else:
            del items[item_id]
            return {"message": f"Item id: {item_id} is deleted"}
