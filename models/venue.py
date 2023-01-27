from db import db


class VenueModel(db.Model):  # type: ignore
    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    items = db.relationship("ItemModel", back_populates="venue", lazy="dynamic", cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="venue", lazy="dynamic", cascade="all, delete")
