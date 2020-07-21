#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])

__SLOTH__.set_offset([0,0,0,0])


def forever():
    __SLOTH__.do_action('turn left', 7, 100)
    __SLOTH__.do_action('forward', 5, 100)
    __SLOTH__.do_action('turn right', 7, 100)
    __SLOTH__.do_action('forward', 5, 100)

if __name__ == "__main__":
    while True:
        forever()  