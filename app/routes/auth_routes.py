from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Dummy login (no password check, for demonstration)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', None)
    if not username:
        return jsonify({"msg": "Missing username"}), 400
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)
