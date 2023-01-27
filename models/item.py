from db import db


class ItemModel(db.Model):  # type: ignore
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venues.id"), unique=False, nullable=False
    )
    venue = db.relationship("VenueModel", back_populates="items", )
