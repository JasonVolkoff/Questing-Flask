from flask.json import jsonify
from models.user import User, user_schema, users_schema
from app import app, db
from flask import request

@app.route('/get', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)

@app.route('/add', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']

    users = User(username, email)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)