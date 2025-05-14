from extensions import db
from flask import Flask, Blueprint, jsonify, request
from app.models.CamUsers import CamUsers 
from config import Config
from app.decorators.auth_decorators import token_required  # Import token_required
from flask_mysqldb import MySQL
user_bp = Blueprint('user', __name__, url_prefix='/users')

# pn_app = Flask(__name__)

# pn_app.config['MYSQL_HOST'] = Config.MYSQL_HOST
# pn_app.config['MYSQL_USER'] = Config.MYSQL_USER
# pn_app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
# pn_app.config['MYSQL_DB'] = Config.MYSQL_DB
# pn_app.config['MYSQL_PORT'] = Config.MYSQL_PORT
# pn_app.config['MYSQL_UNIX_SOCKET'] = None

# mysql = MySQL(pn_app)

# @user_bp.route('/get-sgusers', methods=['GET'])
# @token_required
# def get_sgusers():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM cam_users")
#     users = cur.fetchall()
#     return jsonify(users), 200

# @user_bp.route('/get-sgusers/<int:user_id>', methods=['GET'])
# @token_required
# def get_users(user_id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM cam_users WHERE users_id = %s", (user_id,))
#     user = cur.fetchone()
#     if user:
#         return jsonify(user), 200
#     else:
#         return jsonify({"error": "User not found"}), 404
    
@user_bp.route('/', methods=['GET'])
@token_required
def get_users():
    users = CamUsers.query.all()
    if not users:
        return jsonify({"error": "No users found"}), 404
    return jsonify([{'id': u.users_id, 'name': u.user_name} for u in users])

# @user_bp.route('/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get_or_404(user_id)
#     return jsonify({'id': user.id, 'name': user.name})

# @user_bp.route('/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'id': new_user.id, 'name': new_user.name}), 201

# @user_bp.route('/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.get_json()
#     user = User.query.get_or_404(user_id)
#     user.name = data['name']
#     db.session.commit()
#     return jsonify({'id': user.id, 'name': user.name})

# @user_bp.route('/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get_or_404(user_id)
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted'})
