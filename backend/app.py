from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin":
        return jsonify({"message": "Login Success"})

    return jsonify({"message": "Invalid Credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
