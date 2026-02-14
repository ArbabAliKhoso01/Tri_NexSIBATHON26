from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"

# ===== MySQL Connection =====
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="noor",   # change if needed
        database="edubase_db"
    )

# ===== Landing Page =====
@app.route('/')
def index():
    return render_template('index.html')

# ===== Signup =====
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])
    email = request.form['email']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username,password,email) VALUES (%s,%s,%s)",
            (username, password, email)
        )
        conn.commit()
        flash("Account created successfully! Please login.", "success")
    except:
        flash("Username already exists!", "danger")

    cursor.close()
    conn.close()
    return redirect(url_for('index'))

# ===== Login =====
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and check_password_hash(user['password'], password):
        session['username'] = user['username']
        flash("Login Successful!", "success")
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid Username or Password!", "danger")
        return redirect(url_for('index'))

# ===== Dashboard =====
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard/basic.html', username=session['username'])
    return redirect(url_for('index'))

# ===== Home =====
@app.route('/home')
def home():
    if 'username' in session:
        return render_template('dashboard/home.html', username=session['username'])
    return redirect(url_for('index'))

# ===== Logout =====
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out successfully!", "info")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
