import time
from envirophat import weather
import connect


"""
    Log temperature from enviro pHat sensor for the rasberry pi
    to an sqlite3 database every 15 minutes
"""

DATABASE_NAME = 'temperature.db'


def temperature_reading():
    """ Retrieve temperature in celsius
        :return: temperature
        :rtype: float
    """
    temperature = weather.temperature()
    return float("{0:.2f}".format(temperature))


while True:
    print("Running ")
    conn = connect.connect(DATABASE_NAME)
    connect.write(conn, temperature_reading())
    connect.close(conn)
    time.sleep(900)
