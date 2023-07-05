import paho.mqtt.client as mqtt
# from scripts.DB.config import cursor
import psycopg2
from scripts.api.servicers.services import service

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test",
    user="postgres",
    password="1234"
)

cursor = conn.cursor
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
        service.create_an_item(str(msg.payload.decode()))

