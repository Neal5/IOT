from scripts.api.servicers.services import Service
from scripts.reports.report_generator import GenerateReports

class Subscriber:
    def on_connect_a(client, userdata, flags, rc):
        """ 
        A function that connects to the publisher 
        params: client, result code, userdata and flags
        output: prints on successful connection and gives the result code
        """
        print(f"Connected with result code {str(rc)}")
        client.subscribe("datagen_a")

    def on_connect_b(client, userdata, flags, rc):
        """ 
        A function that connects to the publisher 
        params: client, result code, userdata and flags
        output: prints on successful connection and gives the result code
        """
        print(f"Connected with result code {str(rc)}")
        client.subscribe("datagen_b")



    def on_message(client,userdata, msg):
        """ 
        A function that on getting the msg prints it 
        params: client, result code, msg that is published
        output:prints recieved message and the message
        """
        topic = msg.topic[8]
        print(f"Received message: {str(msg.payload.decode())}")
        Service.create_an_item(str(msg.payload.decode()))
        GenerateReports.create_report(str(msg.payload.decode()),topic)



