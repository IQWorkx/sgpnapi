from flask import Flask
from .extensions import db, jwt
from .routes import register_routes
from .config import Config
from .routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.models import user, product
        db.create_all()

    register_routes(app)
    app.register_blueprint(auth_bp)

    return app
