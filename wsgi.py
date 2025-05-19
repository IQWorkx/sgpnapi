from flask import Flask
from extensions import db, jwt
from app.routes import register_routes
from config import Config 
import logging
logging.basicConfig(filename='logapp.log', level=logging.INFO)
logging.info("App started")


app = Flask(__name__, template_folder=Config.TEMPLATE_FOLDER , static_folder=Config.STATIC_FOLDER) 
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

# with app.app_context():
#     from app.models import user, product
#     db.create_all()

register_routes(app)

if __name__ == "__main__":
      app.run(debug=True,  port=5000)
# Gunicorn command to run the app
# gunicorn --bind