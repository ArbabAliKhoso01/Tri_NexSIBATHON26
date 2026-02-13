from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db_connection
import bcrypt

app = Flask(__name__)
CORS(app)


# 1-REGISTER API
@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    name = data["name"]
    email = data["email"]
    password = data["password"]
    role = data["role"]

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, hashed_password, role))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "User registered successfully"})


# login api
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        return jsonify({
            "message": "Login successful",
            "user_id": user["user_id"],
            "role": user["role"]
        })
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# create subject API
@app.route("/api/subjects", methods=["POST"])
def create_subject():
    data = request.json
    name = data["name"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO subjects (name) VALUES (%s)", (name,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Subject created successfully"})


# get subjects API
@app.route("/api/subjects", methods=["GET"])
def get_subjects():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(subjects)


if __name__ == "__main__":
    app.run(debug=True)
