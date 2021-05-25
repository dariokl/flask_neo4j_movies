from flask import Blueprint
from flask_restful import Api

movies_bp = Blueprint('movies', __name__, url_prefix='/movies')
movies_api = Api(movies_bp)

from . import routes