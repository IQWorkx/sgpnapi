from flask import Blueprint, render_template
from extensions import db

pn_bp = Blueprint('pn', __name__, url_prefix='/')

@pn_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')