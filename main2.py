import paho.mqtt.client as mqtt
from scripts.MQTT.subscriber import subscriber
if __name__ == "__main__":
   client = mqtt.Client()
   client.on_connect = subscriber.on_connect
   client.on_message = subscriber.on_message

   client.connect("localhost", 1883, 61)
   client.loop_forever()