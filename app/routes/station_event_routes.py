from extensions import db
from flask import Flask, Blueprint, jsonify, request
from config import Config
from app.decorators.auth_decorators import token_required  # Import token_required
from app.services.station_event_service import fetch_station_events
station_bp = Blueprint('station_events', __name__, url_prefix='/station_events')

@station_bp.route('/' , methods=['GET'])
@token_required
def get_station_events():
    event_type_id = request.args.get('event_type_id', type=int)
    line_id = request.args.get('line_id', type=int)
    start_time = request.args.get('start_time', type=str)
    end_time = request.args.get('end_time', type=str)

    results = fetch_station_events(event_type_id, line_id, start_time, end_time)
    if not results:
        return jsonify({"error": "No station events found"}), 404
    return jsonify([dict(row._mapping) for row in results])