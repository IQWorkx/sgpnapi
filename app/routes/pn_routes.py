from flask import Blueprint, jsonify, request
from extensions import db
from flask import render_template

pn_bp = Blueprint('pn', __name__, url_prefix='/pn')

@pn.route('/', methods=['GET'])
def index():
    return render_template('index.html')