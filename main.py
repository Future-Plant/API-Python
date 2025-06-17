from fastapi import FastAPI
from app.routes import user, sensor, device, forecast, valve
from app.services.mqtt_subscriber import start_mqtt_subscriber
from app.services.mqtt_simulator import simulate_sensor_data
import threading

app = FastAPI()

# Roteadores da API
app.include_router(user.router)
app.include_router(sensor.router)
app.include_router(device.router)
app.include_router(forecast.router)
app.include_router(valve.router)

# Inicia o subscriber MQTT
start_mqtt_subscriber()

# Inicia o simulador em uma thread separada
threading.Thread(target=simulate_sensor_data, daemon=True).start()

@app.get("/")
def root():
    return {"message": "API IoT Online"}
