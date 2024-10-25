from typing import Annotated, Optional
from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

class SHotelSearchArgs():
    def __init__(
            self,
        location: str,
        date_from: str,
        date_to: str,
        has_spa: Annotated[Optional[bool], Query()] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
            ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars

@app.get("/hotel")
def get_hotel( search_args: SHotelSearchArgs = Depends()):
    return search_args

@app.get("/hotels")

def get_hotels() -> list[SHotel]:
    hotels = [
            {
                "address": "Address A",
                "name": "Hotel A",
                "stars": 5
                },
            ]
    return hotels

class Booking(BaseModel):
    date_from: date
    date_to: date
    room: str

@app.post("/booking")
def add_booking(booking: Booking):
    pass
