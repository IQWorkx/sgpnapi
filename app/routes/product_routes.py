from flask import Blueprint, jsonify, request
from app.models.product import Product
from extensions import db

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'title': p.title} for p in products])

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'title': product.title})

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(title=data['title'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'id': new_product.id, 'title': new_product.title}), 201

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    product.title = data['title']
    db.session.commit()
    return jsonify({'id': product.id, 'title': product.title})

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})
