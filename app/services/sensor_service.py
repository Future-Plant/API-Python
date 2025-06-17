from app.models.sensor import SensorData
from app.database.mongo import db

def create_sensor_data(data: SensorData):
    db.sensor_data.insert_one(data.dict())
    return {"msg": "Dados inseridos"}

def get_sensor_data():
    return list(db.sensor_data.find({}, {"_id": 0}))
