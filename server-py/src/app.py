from flask import Flask,render_template
from extensions import mongo
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo.init_app(app)

from home import home as home_bp
app.register_blueprint(home_bp)

from rate_limiter import rate_limiter as rate_limiter_bp
app.register_blueprint(rate_limiter_bp)

@app.route('/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'
    