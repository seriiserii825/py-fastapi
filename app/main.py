from fastapi import FastAPI

app = FastAPI()

@app.get("/hotels")

def get_hotels():
    return {"hotels": "List of hotels"}
