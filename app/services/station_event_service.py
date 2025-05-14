from sqlalchemy.orm import aliased
from sqlalchemy import func, and_
from app.models import StationEventLog, StationEvent, PartFamily, PartNumber, EventType, EventCategory
from extensions import db

# app/services/station_event_service.py
def fetch_station_events(event_type_id, line_id , start_time, end_time):
    # Aliases for subqueries (optional, can use joins too)
    etype = aliased(EventType)
    ecat = aliased(EventCategory)

    query = (
        db.session.query(
            StationEventLog.line_id,
            StationEventLog.event_seq,
            StationEventLog.event_type_id,
            StationEventLog.tt,
            etype.event_type_name.label('e_type'),
            ecat.events_cat_name.label('cat_name'),
            PartNumber.part_number.label('p_num'),
            PartNumber.part_name.label('p_name'),
            PartFamily.part_family_name.label('pf_name'),
            StationEventLog.created_by,
            StationEventLog.created_on.label('start_time'),
            StationEventLog.end_time,
            StationEventLog.total_time,
            StationEventLog.station_event_log_id,
            StationEventLog.station_event_id
        )
        .join(StationEvent, StationEventLog.station_event_id == StationEvent.station_event_id)
        .join(PartFamily, StationEvent.part_family_id == PartFamily.pm_part_family_id)
        .join(PartNumber, StationEvent.part_number_id == PartNumber.pm_part_number_id)
        .join(etype, etype.event_type_id == StationEventLog.event_type_id)
        .join(ecat, ecat.events_cat_id == StationEventLog.event_cat_id)
        .filter(
            StationEventLog.ignore_id == 0,
            func.date_format(StationEventLog.created_on, '%Y-%m-%d %H:%i') >= start_time,
            func.date_format(StationEventLog.created_on, '%Y-%m-%d %H:%i') <= end_time,
            StationEventLog.event_type_id == event_type_id,
            StationEventLog.line_id == line_id
        )
        .order_by(StationEventLog.created_on.asc())
    )
    return query.all()
    # results = query.all()
    # data = [dict(row._mapping) for row in results]