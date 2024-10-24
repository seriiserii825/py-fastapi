from typing import Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

app = FastAPI()

@app.get("/hotel")

def get_hotel(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
        ):
    return {
            "location": location,
            "date_from": date_from,
            "date_to": date_to,
            "has_spa": has_spa,
            "stars": stars
            }

class Booking(BaseModel):
    date_from: date
    date_to: date
    room: str

@app.post("/booking")
def add_booking(booking: Booking):
    pass
