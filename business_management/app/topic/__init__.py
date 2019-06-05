from flask import Blueprint

tbp = Blueprint("topic", __name__)
from . import views
