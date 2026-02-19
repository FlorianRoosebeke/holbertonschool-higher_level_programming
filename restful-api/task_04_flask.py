#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def get_data():
    return jsonify(users)


@app.route("/status")
def get_status():
    return "<p>OK!</p>"


@app.route("/users/<username>")
def get_profil(username):
    if username in users:
        return users[username], 200
    else:
        return ({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def post_adduser():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400

    username = request.json.get("username")

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    new_user = {
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "city": request.json.get("city")
    }

    users[username] = new_user

    return jsonify({
        "message": "User added successfully",
        "user": {username: new_user}
    }), 201


if __name__ == "__main__":
    app.run()
