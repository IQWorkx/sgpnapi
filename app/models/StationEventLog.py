from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StationEventLog(Base):
    __tablename__ = 'sg_station_event_log'

    station_event_log_id = Column(Integer, primary_key=True, autoincrement=True)
    event_seq = Column(Integer, nullable=True, default=None)
    station_event_id = Column(Integer, nullable=False)
    line_id = Column(Integer, nullable=False)
    event_cat_id = Column(Integer, nullable=True, default=None)
    event_type_id = Column(Integer, nullable=False)
    event_status = Column(String(255), nullable=False, default='1')
    reason = Column(String(150), nullable=True, default=None)
    created_on = Column(String(255), nullable=True, default=None)
    end_time = Column(String(255), nullable=True, default=None)
    tt = Column(String(255), nullable=True, default=None)
    total_time = Column(String(255), nullable=True, default=None)
    created_by = Column(Integer, nullable=True, default=None)
    ignore_id = Column(CHAR(1), nullable=False, default='0')
    is_incomplete = Column(CHAR(1), nullable=True, default=None)