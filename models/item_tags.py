from db import db


class ItemTags(db.Model):  # type: ignore
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(
        db.Integer, db.ForeignKey("items.id"), unique=False, nullable=False
    )
    tag_id = db.Column(
        db.Integer, db.ForeignKey("tags.id"), unique=False, nullable=False
    )