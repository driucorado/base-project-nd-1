
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .engine import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
