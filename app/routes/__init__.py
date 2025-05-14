from .user_routes import user_bp
from .pn_routes import pn_bp
from .station_event_routes import station_bp

def register_routes(app):
    app.register_blueprint(station_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(pn_bp)

