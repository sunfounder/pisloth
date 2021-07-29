from pisloth import Sloth
# from robot_hat import Music
# from robot_hat import TTS
from robot_hat import PWM
from robot_hat import Servo

import sys
import tty
import termios
import time

sloth = Sloth([1,2,3,4])
# tts = TTS()
# music = Music()
sloth.set_offset([0,0,0,0])

right_up_servo = Servo(PWM('P0'))
right_down_servo = Servo(PWM('P1'))
left_up_servo = Servo(PWM('P2'))
left_down_servo = Servo(PWM('P3'))


def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

manual = '''
Press keys on keyboard to control PiSloth!
    Q: Increase left-up servo angle
    W: Decrease left-up servo angle
    Z: Increase left-down servo angle 
    X: Decrease left-down servo angle
    I: Increase right-up servo angle
    O: Decrease right-up servo angle
    N: Increase right-down servo angle
    M: Decrease right-down servo angle    
    SPACE: Print all angle
    ESC: Quit
'''

def main():
    print(manual)
        
    left_up_angle=0
    left_down_angle=0
    right_up_angle=0
    right_down_angle=0
    while True:
        key = readkey()
        # print(key)
        if key == "q":
            left_up_angle = left_up_angle+5
        elif key == "w":
            left_up_angle = left_up_angle-5
        elif key == "z":
            left_down_angle = left_down_angle+5
        elif key == "x":
            left_down_angle = left_down_angle-5
        elif key == "i":
            right_up_angle = right_up_angle+5
        elif key == "o":
            right_up_angle = right_up_angle-5
        elif key == "n":
            right_down_angle = right_down_angle+5
        elif key == "m":
            right_down_angle = right_down_angle-5
        elif key == chr(32): # 32 for space
            print(right_up_angle,right_down_angle,left_up_angle,left_down_angle)
        elif key == chr(27): # 27 for ESC
            break

        right_up_servo.angle(right_up_angle) 
        right_down_servo.angle(right_down_angle) 
        left_up_servo.angle(left_up_angle) 
        left_down_servo.angle(left_down_angle) 
        # time.sleep(0.05)

    print("\nQuit")

if __name__ == "__main__":
    main()  