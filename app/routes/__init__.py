from .user_routes import user_bp
from .product_routes import product_bp
from .pn_routes import pn_bp

def register_routes(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(pn_bp)
