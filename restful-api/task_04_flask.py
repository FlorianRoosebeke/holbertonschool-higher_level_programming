#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Home route - displays a welcome message.

    Returns:
        str: Welcome message in HTML.
    """
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def get_data():
    """Retrieve all users data.

    Returns:
        JSON: Dictionary of all users.
    """
    return jsonify(users)


@app.route("/status")
def get_status():
    """Check API health status.

    Returns:
        str: Status message in HTML.
    """
    return "<p>OK!</p>"


@app.route("/users/<username>")
def get_profil(username):
    """Get user profile by username.

    Args:
        username (str): The username to retrieve.

    Returns:
        tuple: User data with 200 status code, or error 404 if not found.
    """
    if username in users:
        return users[username], 200
    else:
        return ({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def post_adduser():
    """Add a new user to the database.

    Expects JSON with fields: username (required), name, age, city.

    Returns:
        JSON: Confirmation message with user data (201 created).
        Errors:
            400: Missing JSON or username field.
            409: Username already exists.
    """
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
