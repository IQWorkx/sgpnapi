from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import db_config
import datetime
from functools import wraps
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

app = Flask(__name__)

app.config['MYSQL_HOST'] = db_config.MYSQL_HOST
app.config['MYSQL_USER'] = db_config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = db_config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = db_config.MYSQL_DB
app.config['MYSQL_PORT'] = db_config.MYSQL_PORT

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.config['SECRET_KEY'] = 'HTS_S@@rgummi@2025'  # Change this in production

# Token validation function
def get_jwt_payload():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return None, "Missing or invalid Authorization header"

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return payload, None
    except ExpiredSignatureError:
        return None, "Token expired"
    except InvalidTokenError:
        return None, "Invalid token"
    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        payload, error = get_jwt_payload()
        if error:
            return jsonify({'message': error}), 401
        return f(payload, *args, **kwargs)  # Pass payload to route
    return decorated

def is_token_valid(token: str) -> bool:
    try:
        jwt.decode(token,  app.config['SECRET_KEY'], algorithms=["HS256"])
        return True
    except (ExpiredSignatureError, InvalidTokenError, Exception):
        return False
        
def is_valid_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('jwt_token')  # or from header
        if not token or not is_token_valid(token):
            return jsonify({'message': 'Invalid or missing token'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/get-sgusers', methods=['GET'])
@is_valid_token
def get_sgusers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cam_users")
    users = cur.fetchall()
    return jsonify(users), 200

@app.route('/get-sgusers/<int:user_id>', methods=['GET'])
@token_required
def get_users(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cam_users WHERE users_id = %s", (user_id,))
    user = cur.fetchone()
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     email = request.form['email']
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
#     mysql.connection.commit()
#     return jsonify({"status": "User added"}), 200


if __name__ == '__main__':
    app.run(debug=True,  port=5000)
