# Project README

## Description
This project aims to create device simulators to simulate 4-5 energy parameters using MQTT-based Pub-Sub architecture. The simulated data will be stored in a Timescale DB for further analysis and processing.

## Installation
To install the necessary requirements for this project, please follow the steps below:

1. Make sure you have Python installed on your system (Python 3.6 or higher is recommended).
2. Clone the project repository from [GitHub](https://github.com/your-repo-url).
3. Navigate to the project directory:
   ```bash
   cd project-directory
4. Install the required packages using
   ```bash
   pip install -r requirements.txt
5. Install the mosquito from [mosquito](https://mosquitto.org/download/) and activate it as a service according to the instrutions for your OS
6. Install timescaledb according to your postgres version and OS from [timescale](https://docs.timescale.com/self-hosted/latest/install/)
7. Run the createdb.py file after changing the engine string in database.py according to your database
8. Convert the normal table into a hypertable using
   ```bash
    SELECT create_hypertable('timescale_iot','datetime');
9. run the main file using the terminal by
    ```bash
    python main.py COMMAND
