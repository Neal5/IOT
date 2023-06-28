import paho.mqtt.client as mqtt

class subscriber:
    def on_connect(client, userdata, flags, rc):
        """ 
        A function that connects to the publisher 
        params: client, result code, userdata and flags
        output: prints on successful connection and gives the result code
        """
        print(f"Connected with result code {str(rc)}")
        client.subscribe("datagen")


    def on_message(client,userdata, msg):
        """ 
        A function that on getting the msg prints it 
        params: client, result code, msg that is published
        output:prints recieved message and the message
        """
        print(f"Received message: {str(msg.payload.decode())}")


client = mqtt.Client()
client.on_connect = subscriber.on_connect
client.on_message = subscriber.on_message

client.connect("localhost", 1883, 61)
client.loop_forever()

