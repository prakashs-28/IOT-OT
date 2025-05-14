import paho.mqtt.client as mqtt
import time
import random

broker = "192.168.195.128" #kali-1 ip (MQTT broker IP)
port = 1883

client = mqtt.Client(client_id="legit-device")
client.connect(broker, port)

while True:
    # Simulate smart plug ON/OFF
    client.publish("smartplug/on", "ON", qos=0, retain=False)
    
    # Simulate temperature reading
    temp = round(random.uniform(20, 25), 2)
    client.publish("thermostat/temp", str(temp), qos=0, retain=False)
    
    print(f"Sent temp={temp}")
    time.sleep(5)
