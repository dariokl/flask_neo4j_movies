from flask import Blueprint
from flask_restful import Api

movies_bp = Blueprint('videos', __name__, url_prefix='/movie')
movies_api = Api(movies_bp)

from . import routes