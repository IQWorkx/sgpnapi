from flask import Flask
from .extensions import db, jwt
from app.routes import register_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # with app.app_context():
    #     from app.models import user, product
    #     db.create_all()

    register_routes(app)

    return app