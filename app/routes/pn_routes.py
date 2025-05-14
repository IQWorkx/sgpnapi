from flask import Blueprint, jsonify, request
# from app.models.product import Product
from app.extensions import db
from flask import render_template

pn_bp = Blueprint('pn', __name__, url_prefix='/pn')

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'title': p.title} for p in products])

@pn.route('/', methods=['GET'])
def index():
    return render_template('index.html')