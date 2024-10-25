from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String
from app.database import Base

class Rooms(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(ForeignKey("images.id"), nullable=False)
