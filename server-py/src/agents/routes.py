from extensions import mongo
from agents import agents
from flask import jsonify
from datetime import datetime

@agents.route("/agent_test")
def get_agent_response(temp):
    

    return jsonify(temp)