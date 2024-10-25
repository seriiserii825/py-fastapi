from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Integer, String
from app.database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
