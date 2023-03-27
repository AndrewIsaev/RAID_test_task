from flask_cors import CORS
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.frameworks import framework_ns


def create_app(config_object: Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_namespace(framework_ns)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    cors.init_app(app)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
