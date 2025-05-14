from flask import Blueprint, request , jsonify
from config import Config
from functools import wraps
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Token validation function
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({'message': 'Missing or invalid Authorization header'}), 401
        token = auth_header.split(" ")[1]
        if not token:
            return jsonify({'message': 'Missing token'}), 401
        try:
            payload=jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        except (ExpiredSignatureError, InvalidTokenError):
            return jsonify({'message': 'Token has expired or is invalid'}), 401
        except Exception as e:
            return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated     