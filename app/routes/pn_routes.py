from flask import Blueprint, jsonify, request , render_template
from extensions import db

pn_bp = Blueprint('pn', __name__, url_prefix='/pn')

@pn_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')