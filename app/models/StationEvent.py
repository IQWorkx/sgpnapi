from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StationEvent(Base):
    __tablename__ = 'sg_station_event'

    station_event_id = Column(Integer, primary_key=True, autoincrement=True)
    line_id = Column(Integer, nullable=False, index=True)
    part_family_id = Column(Integer, ForeignKey('part_family.pm_part_family_id'), nullable=False, index=True)
    part_number_id = Column(Integer, ForeignKey('part_number.pm_part_number_id'), nullable=False, index=True)
    event_type_id = Column(Integer, ForeignKey('event_type.event_type_id'), nullable=False, index=True)
    event_status = Column(String(255), nullable=False, default='1', index=True)
    reason = Column(String(150), nullable=True)
    created_on = Column(String(255), nullable=True)
    created_by = Column(Integer, nullable=True, index=True)
    modified_on = Column(String(255), nullable=True)
    modified_by = Column(Integer, nullable=True, index=True)