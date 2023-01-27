from marshmallow import Schema, fields


class VenueSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
