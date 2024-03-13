from flask import Blueprint

home = Blueprint('home', __name__)

from src.home import routes