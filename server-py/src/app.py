from flask import Flask,render_template
from extensions import mongo, client
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

client.api_key=os.getenv("OPENAI_API_KEY")


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo.init_app(app)

from home import home as home_bp
app.register_blueprint(home_bp)

from rate_limiter import rate_limiter as rate_limiter_bp
app.register_blueprint(rate_limiter_bp)

from agents import agents as agents_bp
app.register_blueprint(agents_bp)

    