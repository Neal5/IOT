from scripts.Device.data_generator.Data_Genrator import GenerateData
import paho.mqtt.client as mqtt
from scripts.Device.subscriber import Subscriber
import typer

app = typer.Typer()

@app.command()
def simulate_data_a():
    GenerateData.simulate_data_a()

@app.command()
def simulate_data_b():
    GenerateData.simulate_data_b()

@app.command()
def connect_and_listen_a():
    client = mqtt.Client()
    client.on_connect = Subscriber.on_connect_a
    client.on_message = Subscriber.on_message
    client.connect("localhost", 1883, 61)
    client.loop_forever()

@app.command()
def connect_and_listen_b():
    client = mqtt.Client()
    client.on_connect = Subscriber.on_connect_b
    client.on_message = Subscriber.on_message
    client.connect("localhost", 1883, 61)
    client.loop_forever()
