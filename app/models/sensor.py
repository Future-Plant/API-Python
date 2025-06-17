from pydantic import BaseModel
from datetime import datetime

class SensorData(BaseModel):
    umidade: float
    temperatura: float
    timestamp: datetime
