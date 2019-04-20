from envirophat import weather


def temperature_reading():
    """ Retrieve temperature in celsius
        :return: temperature
        :rtype: float
    """
    temperature = weather.temperature()
    return float("{0:.2f}".format(temperature))


def main():
    print(temperature_reading())

if __name__ == '__main__':
    main()
