DIY Action2
===============

通过上一课，我们了解了如何用 ``add_action`` 函数自定义pisloth的动作。这节课我们会通过键盘直接控制pisloth腿部的四个舵机，可以让你
对pisloth的腿部舵机有更直观的理解从而帮助你自定义一些更有趣的动作。

**Code**

.. code:: python

    from robot_hat import PWM
    from robot_hat import Servo

    import sys
    import termios
    import time


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

        print("\nQuit")

    if __name__ == "__main__":
        main()  

**How it works?**

本程序分为两个部分，第一个部分读取按下的键盘的字符，第二部分是通过按下的键盘字符来控制四个舵机。

``left_up_angle`` , ``left_down_angle`` , ``right_up_angle`` , 
``right_down_angle`` 分别对应着函数 ``add_action`` 二维数组参数
里面的四个值。我们通过按下预先设定好的键盘字符，来增加或减少这四个值从而控制
pisloth腿部四个舵机的转动方向和幅度。

.. code:: python

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