#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from sloth import Sloth
__SLOTH__ = Sloth([1,2,3,4])

servoAngle = None

"""Describe this function...

"""

def forever():
    global servoAngle
    servoAngle = [0,0,0,0]         #You can change the STEP of PiSloth by modifying the value of this list.
    __SLOTH__.servo_write_all([(servoAngle[0]),(servoAngle[1]),(servoAngle[2]),(servoAngle[3])])

if __name__ == "__main__":
    while True:
        forever()  