from datetime import datetime
from sqlalchemy import JSON, Column, Computed, Date, DateTime, ForeignKey, Integer, String
from app.database import Base

class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(ForeignKey("rooms.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_costs = Column(Integer, Computed("price * (date_to - date_from)"))
    total_days = Column(Integer, Computed("date_to - date_from"))
