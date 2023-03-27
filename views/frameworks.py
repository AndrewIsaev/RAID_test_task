from flask import request
from flask_restx import Resource, Namespace

from models.framework import FrameworkSchema, FrameworkModel
from setup_db import db

framework_ns = Namespace("frameworks")


@framework_ns.route("/")
class FrameworksView(Resource):
    def get(self):
        frameworks_list = db.session.query(FrameworkModel).all()
        return FrameworkSchema(many=True).dump(frameworks_list), 200


@framework_ns.route("/<language>")
class FrameworkView(Resource):
    def get(self, language):
        frameworks_list = db.session.query(FrameworkModel).filter(FrameworkModel.language == language).all()
        return FrameworkSchema(many=True).dump(frameworks_list), 200
