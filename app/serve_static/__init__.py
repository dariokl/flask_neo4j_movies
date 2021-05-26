from flask import Blueprint


static_bp = Blueprint('staticbp', __name__, url_prefix='/')

from . import views