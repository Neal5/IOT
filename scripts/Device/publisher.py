import logging

import paho.mqtt.client as mqtt

class Publisher:
    def on_connect(client, userdata, flags, rc):
        """ 
        A function that on connecting gives info of the connect
        params: client, result code, uesrdata and the flags
        output:prints connected and the result code
        """
        try:
            logging.info(f"Connected with result code {str(rc)}")
        except Exception as e:
            logging.exception(e)

    def publish(message,device):
        """ 
        A function to publish the given message
        params: message that needs to be published
        output:publishes the message and prints prints published and the given messag
        """
        try:
            
            client = mqtt.Client()
            client.on_connect = Publisher.on_connect
            client.connect("localhost", 1883, 61)
            client.loop_start()
            client.publish("datagen_"+device, message)
            print("published",message,"\n")
        except Exception as e:
            logging.exception(e)
