from fastapi import FastAPI
from app.routes import user, sensor, device, forecast
from app.services.mqtt_subscriber import start_mqtt_subscriber

app = FastAPI()

app.include_router(user.router)
app.include_router(sensor.router)
app.include_router(device.router)
app.include_router(forecast.router)

start_mqtt_subscriber()

@app.get("/")
def root():
    return {"message": "API IoT Online"}
