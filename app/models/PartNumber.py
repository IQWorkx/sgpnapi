from sqlalchemy import Column, Integer, String, CHAR, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PartNumber(Base):
    __tablename__ = 'pm_part_number'

    pm_part_number_id = Column(Integer, primary_key=True, autoincrement=True)
    part_number = Column(String(255), nullable=True)
    part_name = Column(String(255), nullable=True)
    customer_part_number = Column(String(255), nullable=True)
    station = Column(String(255), nullable=True)
    part_family = Column(Integer, ForeignKey('part_family.pm_part_family_id'), nullable=True)
    part_images = Column(Text, nullable=True)
    npr = Column(String(255), nullable=True)
    through_put = Column(String(255), nullable=True)
    budget_scrape_rate = Column(String(255), nullable=True)
    net_weight = Column(String(255), nullable=True)
    part_length = Column(String(255), nullable=True)
    length_range = Column(String(255), nullable=True)
    notes = Column(String(255), nullable=True)
    color_code = Column(String(50), nullable=True)
    available_stock = Column(Integer, nullable=False, default=0)
    created_by = Column(String(255), nullable=True)
    is_deleted = Column(CHAR(1), nullable=False, default='0')
    defect_part_images = Column(Text, nullable=True)
    part_defect_zone = Column(String(255), nullable=True)