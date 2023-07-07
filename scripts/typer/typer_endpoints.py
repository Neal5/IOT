from scripts.Device.data_generator.Data_Genrator import GenerateData
import paho.mqtt.client as mqtt
from scripts.Device.subscriber import Subscriber
import typer
import logging
app = typer.Typer()

@app.command()
def simulate_data_a():
    """ 
        A function that on being called using the command calls the function simulate_data_a
        params: NA
        output: NA
    """
    try:
        GenerateData.simulate_data_a()
    except Exception as e:
        logging.exception(e)

@app.command()
def simulate_data_b():
    """ 
        A function that on being called using the command calls the function simulate_data_b
        params: NA
        output: NA
    """
    try:
        GenerateData.simulate_data_b()
    except Exception as e:
        logging.exception(e)

@app.command()
def connect_and_listen_a():
    """ 
        A function that on being called using the command subscribes to data for a
        params: NA
        output: NA
    """
    try:
        client = mqtt.Client()
        client.on_connect = Subscriber.on_connect_a
        client.on_message = Subscriber.on_message
        client.connect("localhost", 1883, 61)
        client.loop_forever()
    except Exception as e:
        logging.exception(e)

@app.command()
def connect_and_listen_b():
    """ 
        A function that on being called using the command subscribes to data for b
        params: NA
        output: NA
    """
    try:
        client = mqtt.Client()
        client.on_connect = Subscriber.on_connect_b
        client.on_message = Subscriber.on_message
        client.connect("localhost", 1883, 61)
        client.loop_forever()
    except Exception as e:
        logging.exception(e)
