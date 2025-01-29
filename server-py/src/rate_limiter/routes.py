from extensions import mongo
from rate_limiter import rate_limiter
from flask import jsonify
from datetime import datetime

def get_data(data):
     data['_id'] = str(data['_id'])
     return data

@rate_limiter.route("/user")
def add_user():
    new_user = {
        "first_name": "Tom",
        "last_name": "Foolory",
        "email": "tifff@gmail.com",
        "date": datetime.now(),
    }

    users = mongo.db.users
    existing_user = users.find_one()
    if not existing_user:
        user_id = users.insert_one(new_user).inserted_id
        print(user_id)
    temp = [get_data(existing_user)]
    return jsonify(temp)

@rate_limiter.route("/pyarrow")
def pyarrow():
    data = mongo.db.data

    existing_data = data.find()
    if not existing_data:
        existing_data = data.insert_many([
            {'_id': 11, 'amount': 21, 'last_updated': datetime(2020, 12, 10, 1, 3, 1), 'account': {'name': 'Customer1', 'account_number': 1}, 'txns': ['A']},
            {'_id': 12, 'amount': 16, 'last_updated': datetime(2020, 7, 23, 6, 7, 11), 'account': {'name': 'Customer2', 'account_number': 2}, 'txns': ['A', 'B']},
            {'_id': 13, 'amount': 3,  'last_updated': datetime(2021, 3, 10, 18, 43, 9), 'account': {'name': 'Customer3', 'account_number': 3}, 'txns': ['A', 'B', 'C']},
            {'_id': 14, 'amount': 0,  'last_updated': datetime(2021, 2, 25, 3, 50, 31), 'account': {'name': 'Customer4', 'account_number': 4}, 'txns': ['A', 'B', 'C', 'D']}])
    

    result = data.update_many({"test": {"$exists": False}}, {"$set": {"test": False}})

    return jsonify(result.raw_result)
