from db import db


class TagModel(db.Model):  # type: ignore
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.id"), unique=False, nullable=False)
    venue = db.relationship(
        "VenueModel",
        back_populates="tags",
    )
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")
