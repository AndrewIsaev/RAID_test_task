from setup_db import db

from marshmallow import Schema, fields


class FrameworkModel(db.Model):
    __tablename__ = "frameworks"
    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    language = db.Column(db.String(100), nullable=False)


class FrameworkSchema(Schema):
    pk = fields.Int()
    name = fields.Str()
    language = fields.Str()
