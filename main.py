# main.py -- put your code here!
import display, sensors
import pyb

config = {
    'orientation': 'X',
    'connected_pin': 'Y11'}

d = display.Display(config)
s = sensors.GP2Y0A02YK0F(config)
sw = pyb.Switch()

sw.callback(d.toggle_display)

while True:
    d.get_touch()
    pyb.delay(1000)
