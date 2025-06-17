import threading
import time
import json
import random
import paho.mqtt.publish as publish
from datetime import datetime

def simulate_sensor_data():
    while True:
        umidade = round(random.uniform(40, 70), 2)         # Ex: 55.32
        temperatura = round(random.uniform(20, 35), 2)     # Ex: 27.89
        timestamp = datetime.now().isoformat()

        payload = {
            "umidade": umidade,
            "temperatura": temperatura,
            "timestamp": timestamp
        }

        try:
            publish.single(
                topic="fatec/iot/umidade",
                payload=json.dumps(payload),
                hostname="test.mosquitto.org"
            )
            print("[Simulador] Publicado:", payload)
        except Exception as e:
            print("[Simulador] Falha ao publicar:", e)

        time.sleep(5)  # Aguarda 5 segundos antes de gerar outro dado
