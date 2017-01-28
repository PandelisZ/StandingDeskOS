import lcd160cr


class Display():

    colo = {
        'black': 0,
        'white': 65535}

    def __init__(self, config):
        self.lcd = lcd160cr.LCD160CR(config['orientation'])
        self.lcd.set_pen(self.colo['white'], self.colo['black'])
        self.lcd.set_orient(lcd160cr.LANDSCAPE)

    def demo(self):
        self.lcd.erase()
        self.lcd.line(0, 0, 90, 90)

    def write(self, text):
        self.lcd.erase()
        self.lcd.set_pos(0, 0)
        self.lcd.set_font(1)
        self.lcd.write(text)
