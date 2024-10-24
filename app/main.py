from typing import Optional
from fastapi import FastAPI, Query
from datetime import date

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
