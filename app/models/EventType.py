from sqlalchemy import Column, Integer, String, CHAR, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventType(Base):
    __tablename__ = 'event_type'

    event_type_id = Column(Integer, primary_key=True, autoincrement=True)
    event_type_name = Column(String(255), nullable=True)
    event_cat_id = Column(Integer, ForeignKey('event_category.events_cat_id'), nullable=False, default=1)
    stations = Column(Text, nullable=True)
    color_code = Column(String(255), nullable=False, default='#218838')
    so = Column(Integer, nullable=False)
    created_at = Column(String(255), nullable=True)
    updated_at = Column(String(255), nullable=True)
    is_deleted = Column(CHAR(1), nullable=False, default='0')