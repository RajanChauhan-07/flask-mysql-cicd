from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
import time

app = Flask(__name__)

# Database configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'mysql'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'rootpassword'),
    'database': os.getenv('DB_NAME', 'flaskdb')
}


def get_db_connection():
    """Create and return a database connection with retry logic"""
    max_retries = 5
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            if connection.is_connected():
                print("Successfully connected to MySQL database")
                return connection
        except Error as e:
            print(f"Connection attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise
    return None


@app.route('/')
def index():
    """Main page - display all users"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', users=users)
    except Error as e:
        return f"Database Error: {e}", 500


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the database"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'User added successfully'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint for testing"""
    try:
        connection = get_db_connection()
        if connection and connection.is_connected():
            connection.close()
            return jsonify({'status': 'healthy', 'database': 'connected'}), 200
    except Error as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
