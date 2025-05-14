from sqlalchemy import Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PartFamily(Base):
    __tablename__ = 'pm_part_family'

    pm_part_family_id = Column(Integer, primary_key=True, autoincrement=True)
    part_family_name = Column(String(255), nullable=True, index=True)
    station = Column(Integer, nullable=True, index=True)
    notes = Column(String(255), nullable=True)
    created_by = Column(String(255), nullable=True)
    is_deleted = Column(CHAR(1), nullable=False, default='0')
    image_path = Column(String(255), nullable=True)