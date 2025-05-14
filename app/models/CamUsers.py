from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CamUsers(Base):
    __tablename__ = 'cam_users'

    users_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<CamUsers(id={self.id}, username='{self.username}', email='{self.email}')>"