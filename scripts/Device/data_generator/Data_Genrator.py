import time
import logging
import pandas as pd
import numpy as np
# from publisher import Publisher
from scripts.Device.publisher import Publisher
import asyncio
class GenerateData:

    def simulate_data_fastapi(no):
        """ 
        A function that converts the given csv file into a dataframe creates a new dataframe containing only the parameters and the randomly generated value between the given limits and publishes a string using the publish method defined in scripts.MQTT.publisher
        params: Uses the energy_meter_limit.csv in the parameters folder
        output:publishes a string using the publish method defined in scripts.MQTT.publisher
        """
        try:
            for i in range(int(no)):
                path = "scripts\Device\parameters\energy_meter_limits_a.csv"
                df = pd.read_csv(path)
                df['random_values'] = df.apply(lambda x: np.random.uniform(x.Lower_Limit, x.Upper_Limit), axis=1)
                df2 = pd.DataFrame().assign(Parameter=df['Parameter'],random_values=df['random_values'])
                df2 = df2.to_json(orient = 'records')
                Publisher.publish(df2,"m")
                # await asyncio.sleep(10)
        except Exception as e:
            logging.exception(e)

    async def simulate_data_a():
        """ 
        A function that converts the given csv file into a dataframe creates a new dataframe containing only the parameters and the randomly generated value between the given limits and publishes a string using the publish method defined in scripts.MQTT.publisher
        params: Uses the energy_meter_limit.csv in the parameters folder
        output:publishes a string using the publish method defined in scripts.MQTT.publisher
        """
        try:
            while True:
                path = "scripts\Device\parameters\energy_meter_limits_a.csv"
                df = pd.read_csv(path)
                df['random_values'] = df.apply(lambda x: np.random.uniform(x.Lower_Limit, x.Upper_Limit), axis=1)
                df2 = pd.DataFrame().assign(Parameter=df['Parameter'],random_values=df['random_values'])
                df2 = df2.to_json(orient = 'records')
                Publisher.publish(df2,"a")
                await asyncio.sleep(10)
        except Exception as e:
            logging.exception(e)

    async def simulate_data_b():
        """ 
        A function that converts the given csv file into a dataframe creates a new dataframe containing only the parameters and the randomly generated value between the given limits and publishes a string using the publish method defined in scripts.MQTT.publisher
        params: Uses the energy_meter_limit.csv in the parameters folder
        output:publishes a string using the publish method defined in scripts.MQTT.publisher
        """
        try:
            while True:
                path = "scripts\Device\parameters\energy_meter_limits_b.csv"
                df = pd.read_csv(path)
                df['random_values'] = df.apply(lambda x: np.random.uniform(x.Lower_Limit, x.Upper_Limit), axis=1)
                df2 = pd.DataFrame().assign(Parameter=df['Parameter'],random_values=df['random_values'])
                df2 = df2.to_json(orient = 'records')
                Publisher.publish(df2,"b")
                await asyncio.sleep(10)
        except Exception as e:
            logging.exception(e)
