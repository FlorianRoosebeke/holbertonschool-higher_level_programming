#!/usr/bin/python3
"""Basic auth and JWT protected API endpoints."""

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """Validate basic auth credentials."""
    if username in users:
        password_hash = users[username]["password"]
        if check_password_hash(password_hash, password):
            return username
    return None


@app.route("/basic-protected")
@auth.login_required
def index():
    """Return a basic-auth greeting."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT token."""
    if request.is_json:
        data = request.get_json()
    else:
        data = {}
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Allow access only for admin users."""
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if not user or user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def protected():
    """Return a JWT-protected greeting."""
    current_user = get_jwt_identity()
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle JWT token that is not fresh."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
