import paho.mqtt.publish as publish

def publish_valve(command: str):
    publish.single("fatec/iot/solenoide", command, hostname="test.mosquitto.org")
    return {"msg": f"Comando '{command}' enviado para válvula"}
