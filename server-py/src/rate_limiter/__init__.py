from flask import Blueprint

rate_limiter = Blueprint('rate_limiter', __name__)

from rate_limiter import routes