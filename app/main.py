from fastapi import FastAPI

app = FastAPI()

@app.get("/hotel/{hotel_id}")

def get_hotel(hotel_id: int, date_from, date_to):
    return {"hotel_id": hotel_id, "date_from": date_from, "date_to": date_to}
