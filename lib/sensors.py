from pyb import Pin, ADC


class GP2Y0A02YK0F():

    mapping = {
        'off': 4014
    }

    pin = None    # Lower-level ADC-connection to the sensor
    height = None # Last checked height (ADC'ed)

    def __init__(self, config):
        self.pin = ADC(Pin(config['connected_pin']))

    def read(self):
        self.height = self.pin.read()
        print(self.height)
