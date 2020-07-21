#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import Pin
from ezblock import Ultrasonic
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])

reference = None

distance = None

reference = 10

pin_D0 = Pin("D0")

pin_D1 = Pin("D1")


def forever():
    global reference, distance
    distance = Ultrasonic(pin_D0, pin_D1).read()
    if distance >= reference:
        __SLOTH__.do_action('forward', 1, 100)
    else:
        __SLOTH__.do_action('backward', 1, 100)
        __SLOTH__.do_action('stop', 1, 100)
        __SLOTH__.do_action('turn right', 1, 100)
        __SLOTH__.do_action('stop', 1, 100)

if __name__ == "__main__":
    while True:
        forever()  