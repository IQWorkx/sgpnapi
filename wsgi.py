from flask import Flask
from extensions import db, jwt
from app.routes import register_routes
from config import Config
from app.routes.auth_routes import auth_bp   

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

# with app.app_context():
#     from app.models import user, product
#     db.create_all()

register_routes(app)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
      app.run(debug=True,  port=5000)
# Gunicorn command to run the app
# gunicorn --bind