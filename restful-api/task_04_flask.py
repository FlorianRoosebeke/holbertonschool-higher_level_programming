#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Home route - displays a welcome message."""
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def get_data():
    """Retrieve all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Check API health status."""
    return "OK"


@app.route("/users/<username>")
def get_profil(username):
    """Get user profile by username."""
    if username in users:
        user_data = users[username].copy()
        user_data["username"] = username
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def post_adduser():
    """Add a new user to the database."""
    try:
        data = request.get_json()
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get("username")

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run()
