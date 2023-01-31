from flask import Flask
from flask_smorest import Api
from resources.venue import blp as VenueBlueprint
from resources.item import blp as ItemBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint


def configure_api(app: Flask):
    api = Api(app)
    api.register_blueprint(VenueBlueprint)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
