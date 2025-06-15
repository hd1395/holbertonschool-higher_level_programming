from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-jwt-key-for-auth"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory dictionary to store user data, including hashed passwords and roles
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@jwt.unauthorized_loader
def unauthorized_response(callback):
    """
    Callback for when a JWT is required but not found or invalid.
    """
    return jsonify({"error": "Missing Authorization Header or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    """
    Callback for when a JWT is malformed.
    """
    return jsonify({"error": "Signature verification failed: Token is invalid"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    """
    Callback for when a JWT has expired.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_response(callback):
    """
    Callback for when a JWT has been revoked.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_response(callback):
    """
    Callback for when a refresh token is needed but not provided.
    """
    return jsonify({"error": "Fresh token required"}), 401

# --- Basic Authentication Callback ---
@auth.verify_password
def verify_password(username, password):
    """
    Verifies the username and password for Basic Authentication.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# --- Routes ---

@app.route("/")
def home():
    """
    Handles the root URL ("/") and returns a welcome message.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_all_usernames():
    """
    Handles the "/data" endpoint and returns a JSON list of all usernames.
    """
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def get_status():
    """
    Handles the "/status" endpoint and returns a simple "OK" message.
    """
    return "OK"

@app.route("/users/<username>")
def get_user_by_username(username):
    """
    Handles the "/users/<username>" endpoint.
    """
    user_data = users.get(username)
    if user_data:
        display_data = user_data.copy()
        display_data.pop("password", None)
        return jsonify(display_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles the "/add_user" endpoint, accepting POST requests.
    Returns a confirmation message with the added user's data.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    new_user_data = request.get_json()

    username = new_user_data.get("username")
    password = new_user_data.get("password")
    role = new_user_data.get("role", "user") # Default role is 'user' if not provided

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if username in users:
        return jsonify({"error": f"User '{username}' already exists"}), 409 # 409 Conflict

    hashed_password = generate_password_hash(password)
    users[username] = {"username": username, "password": hashed_password, "role": role}
    confirmation_data = users[username].copy()
    confirmation_data.pop("password", None)
    return jsonify({"message": "User added", "user": confirmation_data}), 201

@app.route("/basic-protected")
@auth.login_required
def basic_protected_route():
    """
    Returns a message "Basic Auth: Access Granted" if the user provides valid
    basic authentication credentials.
    """
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON payload with username and password.
    Returns a JWT access token if credentials are valid.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token)

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected_route():
    """
    Returns a message "JWT Auth: Access Granted" if the user provides a valid JWT token.
    """
    return f"JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only_route():
    """
    Returns a message "Admin Access: Granted" if the user is an admin.
    Requires a valid JWT token and checks the user's role.
    """
    current_user_identity = get_jwt_identity()
    claims = get_jwt()

    if claims.get("role") == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403

if __name__ == "__main__":
    app.run()
