from flask import Blueprint

ubp = Blueprint("users", __name__)
from . import views