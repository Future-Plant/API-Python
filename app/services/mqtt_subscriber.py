import paho.mqtt.client as mqtt
import json
from app.database.mongo import db

# Callback executada quando chega uma mensagem
def on_message(client, userdata, msg):
    print(f"[MQTT] Tópico: {msg.topic} | Mensagem: {msg.payload.decode()}")

    try:
        dados = json.loads(msg.payload.decode())  # A mensagem deve ser JSON
        db.sensor_data.insert_one(dados)          # Insere no MongoDB
        print("[MongoDB] Dados inseridos:", dados)
    except Exception as e:
        print("[ERRO] Falha ao inserir dados do MQTT:", e)

# Inicia o cliente MQTT como assinante
def start_mqtt_subscriber():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)
    client.subscribe("fatec/iot/umidade")
    client.loop_start()  # Escuta o tópico em segundo plano

