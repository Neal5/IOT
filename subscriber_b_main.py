import paho.mqtt.client as mqtt
from scripts.MQTT.subscriber import Subscriber
if __name__ == "__main__":
   client = mqtt.Client()
   client.on_connect = Subscriber.on_connect_b
   client.on_message = Subscriber.on_message

   client.connect("localhost", 1883, 61)
   client.loop_forever()