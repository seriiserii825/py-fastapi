from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Integer, String
from app.database import Base

class Hotels(Base):
    __tablename__ = "hotels"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
    # created_at = Column(DateTime, default=datetime.now)
    # updated_at = Column(DateTime, default=datetime.now)
    
