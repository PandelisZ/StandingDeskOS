# Standing-Desk-OS

My Operating System for the IKEA electric standing desk *BEKANT*, written in MicroPython


## Intention / Goals

I want to improve the standing desk by enabling it to arrive at certain heights,
automatically. The desk should then be able to meassure it's current height
and set a direction on its own. When it reaches certain heights, it should act
accordingly. Thresholds could be

* Maximum or minimum heights
* User set favorites
* Maybe a height set by a slider on the touch display


## Components

This project is currently based on the following hardware:

* [The official MicroPython PyBoard](http://docs.micropython.org/en/latest/pyboard/index.html)
* [The LCD160CR OLED touch display](https://docs.micropython.org/en/latest/pyboard/library/lcd160cr.html)
* [A Sharp GP2Y0A02YK0F distance sensor](https://www.sharpsde.com/products/optoelectronic-components/model/GP2Y0A02YK0F) - for distance measurements of 20cm - 150cm
* Obviously, the [IKEA BEKANT electric standing desk](http://www.ikea.com/de/de/catalog/products/S69022537/)

Consider buying stuff in the [official shop](https://store.micropython.org/#/store) to support the project. The Board and the Display can be bought there.
