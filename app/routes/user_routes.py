from extensions import db
from flask import Flask, Blueprint, jsonify, request
from app.models.CamUsers import CamUsers 
from config import Config
from app.decorators.auth_decorators import token_required  # Import token_required
user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
@token_required
def get_users():
    users = CamUsers.query.all()
    if not users:
        return jsonify({"error": "No users found"}), 404
    return jsonify([{'id': u.users_id, 'name': u.user_name} for u in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
@token_required
def get_user_by_id(user_id):
    user = CamUsers.query.get_or_404(user_id)
    return jsonify({'id': user.users_id, 'name': user.user_name})

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
