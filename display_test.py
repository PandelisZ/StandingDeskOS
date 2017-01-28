import lcd160cr

# Colors
black = 0
white = 65535


def run_test():
    lcd = lcd160cr.LCD160CR('X')
    lcd.set_pen(white, black)
    lcd.erase()
    lcd.line(0, 0, 90, 90)


if __name__ == '__main__':
    run_test()
