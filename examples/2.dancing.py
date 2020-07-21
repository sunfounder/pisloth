#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])


def forever():
    __SLOTH__.do_action('moon walk left', 2, 100)
    __SLOTH__.do_action('moon walk right', 2, 100)
    __SLOTH__.do_action('turn right', 1, 100)
    __SLOTH__.do_action('shake left', 1, 100)
    __SLOTH__.do_action('turn left', 1, 100)
    __SLOTH__.do_action('shake right', 1, 100)
    __SLOTH__.do_action('go up and down', 1, 100)
    __SLOTH__.do_action('swing', 1, 100)
    __SLOTH__.do_action('big swing', 1, 100)
    __SLOTH__.do_action('stop', 1, 50)

if __name__ == "__main__":
    while True:
        forever()  