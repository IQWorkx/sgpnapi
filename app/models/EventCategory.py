from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventCategory(Base):
    __tablename__ = 'events_category'

    events_cat_id = Column(Integer, primary_key=True, autoincrement=True)
    events_cat_name = Column(String(255), nullable=True)
    npr = Column(CHAR(1), nullable=False, default='0')
    created_by = Column(String(255), nullable=True)
    created_on = Column(String(255), nullable=True)
    is_deleted = Column(CHAR(1), nullable=False, default='0')