from fastapi import APIRouter, Depends
from app.services.sensor_service import create_sensor_data, get_sensor_data
from app.models.sensor import SensorData
from typing import List

router = APIRouter(prefix="/sensor", tags=["Sensor"])

@router.post("/")
def receive_data(sensor_data: SensorData):
    return create_sensor_data(sensor_data)

@router.get("/", response_model=List[SensorData])
def list_data():
    return get_sensor_data()



