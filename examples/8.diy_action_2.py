#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])
from ezblock import delay

diyAction = None

__SLOTH__.add_action("diyAction", [[0,(-50),0,50], [0,0,0,0], [0,50,0,(-50)], [0,0,0,0]])
diyAction = "diyAction"


def forever():
    global diyAction
    __SLOTH__.do_action(diyAction, 1, 80)
    delay(1000)
	
if __name__ == "__main__":
    while True:
        forever()  