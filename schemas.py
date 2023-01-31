from marshmallow import Schema, fields


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)


class PlainVenueSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemSchema(PlainItemSchema):
    venue_id = fields.Int(required=True, load_only=True)
    venue = fields.Nested(PlainVenueSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True)


class TagSchema(PlainTagSchema):
    venue_id = fields.Int(required=True, load_only=True)
    venue = fields.Nested(PlainVenueSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)


class VenueSchema(PlainVenueSchema):
    items = fields.List(fields.Nested(PlainItemSchema), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema), dump_only=True)


class UpdateItemSchema(Schema):
    name = fields.Str()
    price = fields.Int()
    venue_id = fields.Int()


class UpdateVenueSchema(Schema):
    name = fields.Str()


class TagAndItemSchema(Schema):
    message = fields.Str()
    tag = fields.Nested(TagSchema)
    item = fields.Nested(ItemSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
