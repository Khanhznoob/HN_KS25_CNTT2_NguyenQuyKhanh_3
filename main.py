from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    car_code: str
    type: str
    rental_price: float
    status: str

raw_cars = [
    {"car_code": "C301", "type": "suv",
    "rental_price": 1200000, "status": "available"},
    {"car_code": "c101", "type": "sedan",
         "rental_price": 700000, "status": "available"},
    {"car_code": "C202", "type": "pickup",
         "rental_price": 950000, "status": "rented"},
    {"car_code": "C102", "type": "sedan",
         "rental_price": 650000, "status": "maintenance"},
    {"car_code": "C302", "type": "suv",
         "rental_price": 1500000, "status": "available"},    
]

@app.post("/cars")
def create_car():
    new_car = [
        "car_code" == str,
        "type" == str,
        "rental_price" == float,
        "status" == str
    ]
    raw_cars.append(new_car)
    return new_car

@app.get("/cars")
def get_car():
    return raw_cars

@app.delete("/cars")
def delete_car(car_code: str):
    for car in raw_cars:
        if car["car_code"] == car_code:
            raw_cars.remove(car)
    