import lcd160cr

# Colors
black = 0
white = 65535


class Display(config):

    def __init__(self):
        lcd = lcd160cr.LCD160CR(config.orientation)
        lcd.set_pen(white, black)

    def demo(self):
        lcd = lcd160cr.LCD160CR('X')
        lcd.set_pen(white, black)
        lcd.erase()
        lcd.line(0, 0, 90, 90)

    def draw_ui(self):
        lcd.erase()
        lcd.line(0, 0, 90, 90)
