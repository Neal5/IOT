import logging
from datetime import datetime
import json

class GenerateReports:
    def create_report(data, device):
        """A function that takes data from the subscriber and writes it into a json for the given device
        params: NA
        returns: NA
        """
        try:
            data = json.loads(data)

            converted_data = {}

            for item in data:
                parameter = item["Parameter"]
                value = item["random_values"]
                converted_data[parameter] = value
            converted_data["timestamp"] = str(datetime.now())
            path = "scripts\\Device\\reports\\"
            filename = path + "device_" + device + ".json"
            with open(filename, "a") as json_file: 
                json.dump(converted_data, json_file)
                json_file.write("\n") 
        except Exception as e:
            logging.exception(e)
