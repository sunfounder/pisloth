#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
import random
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])
from ezblock import delay

turn = None

turn = ['turn left', 'turn right', 'stop']


def forever():
    global turn
    __SLOTH__.do_action(random.choice(turn), (random.randint(2, 7)), 100)
    __SLOTH__.do_action('forward', (random.randint(4, 7)), 100)
    __SLOTH__.do_action('stop', 1, 100)
    delay((random.randint(4, 15) * 100))

if __name__ == "__main__":
    while True:
        forever()  