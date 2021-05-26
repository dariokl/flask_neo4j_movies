from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from config import config

api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api.init_app(app)

    cors = CORS(app, resource={'*': {"origins": '*'}})


    from .movies import movies_bp
    from .serve_static import static_bp

    app.register_blueprint(movies_bp)
    app.register_blueprint(static_bp)

    return app