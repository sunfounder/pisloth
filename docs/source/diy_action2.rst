DIY Action2
===============

Through the last lesson, we learned how to customize the action of Pisloth with the ``add_action`` function. In this lesson, we will directly control the four servos of the Pisloth leg through the keyboard, which allows you to
have a more intuitive understanding of Pisloth's leg servos to help you customize some more interesting actions.

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

This program is divided into two parts. The first part reads the characters of the pressed keyboard, and the second part controls the four servos by pressing the characters of the keyboard.

``left_up_angle``, ``left_down_angle``, ``right_up_angle``, ``right_down_angle`` corresponds to the four values ​​in the parameters of the function ``add_action``. We increase or decrease these four values ​​by pressing the preset keyboard characters to control the rotation direction and amplitude of the four servos on the pisloth leg.

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