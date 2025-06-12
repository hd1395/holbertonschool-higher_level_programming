from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory dictionary to store user data
users = {}

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
    return jsonify(list(users.keys()))

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
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles the "/add_user" endpoint, accepting POST requests.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    new_user_data = request.get_json()

    username = new_user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": f"User '{username}' already exists"}), 409

    users[username] = new_user_data

    return jsonify({"message": "User added successfully", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
