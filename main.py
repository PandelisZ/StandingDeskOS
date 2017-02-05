# main.py -- put your code here!
import display, sensors

config = {
    'orientation': 'X',
    'connected_pin': 'Y11'}

d = display.Display(config)
d.write('Hi Boss :)')

s = sensors.GP2Y0A02YK0F(config)
