import lcd160cr


class Display():

    colo = {
        'black': 0,
        'white': 65535}

    def __init__(self, config):
        self.lcd = lcd160cr.LCD160CR(config['orientation'])
        self.lcd.erase()
        self.lcd.set_pen(self.colo['white'], self.colo['black'])
        self.lcd.set_text_color(self.colo['white'], self.colo['black'])
        self.lcd.set_orient(lcd160cr.LANDSCAPE)
        self.lcd.set_font(1)
        self.h_half = round(self.lcd.h/2)
        self.w_half = round(self.lcd.w/2)
        self.draw_menu()

    def draw_menu(self):
        # self.write('W:{} x H:{} -> Disp. Size'.format(self.lcd.w, self.lcd.h))
        self.lcd.line(0, self.h_half, self.lcd.w, self.h_half)           # horizontal line
        self.lcd.line(self.w_half, self.h_half, self.w_half, self.lcd.h) # vertical line
        self.lcd.set_pos(5, self.h_half+5)
        self.lcd.write('GO UP')
        self.lcd.set_pos(self.w_half+5, self.h_half+5)
        self.lcd.write('GO DOWN')

    def demo(self):
        self.lcd.erase()
        self.lcd.line(0, 0, 90, 90)

    def write(self, text):
        self.lcd.erase()
        self.draw_menu()
        self.lcd.set_pos(0, 0)
        self.lcd.write(text+'   ')

    def get_touch(self):
        coords = self.lcd.get_touch()
        self.write('Touched:{} at x:{} y:{}\n'.format(coords[0], coords[1], coords[2]))
