from flask import Flask,render_template
from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.wsgi import WSGIMiddleware
from src.extensions import mongo
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
flask_app = Flask(__name__)

#Mount Flask on FastApi
app.mount("/home", WSGIMiddleware)
flask_app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo.init_app(flask_app)

from src.home import home as home_bp
flask_app.register_blueprint(home_bp)

from src.rate_limiter import rate_limiter as rate_limiter_bp
flask_app.register_blueprint(rate_limiter_bp)

@app.get('/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'

if __name__ == '__init__':
    uvicorn.run(app, host='127.0.0.1', port=8080)