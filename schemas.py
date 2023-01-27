from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)


class PlainVenueSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    venue_id = fields.Int(required=True, load_only=True)
    venue = fields.Nested(PlainVenueSchema(), dump_only=True)


class VenueSchema(PlainVenueSchema):
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)


class UpdateItemSchema(Schema):
    name = fields.Str()
    price = fields.Int()
    venue_id = fields.Int()


class UpdateVenueSchema(Schema):
    name = fields.Str()
