from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_envvar('ENDORSE_CFG')
mongo = PyMongo(app)


@app.route('/add/<username>', methods=['GET'])
def add_user(username):
    users = mongo.db.users
    result = users.insert_one({'_id': username, 'attr': 6})
    return get_user(username)

@app.route('/', methods=['GET'])
def get_users():
    users = mongo.db.users
    user = list(users.find())
    return jsonify(user)

@app.route('/<username>', methods=['GET'])
def get_user(username):
    users = mongo.db.users
    user = users.find_one({'_id': username})
    return jsonify(user)
