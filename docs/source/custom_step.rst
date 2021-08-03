Custom Step
===============

In the previous projects, we used a lot of actions that we wrote, so how are these actions composed and done? Generally speaking, an action is composed of one or more steps.

In this project, we will learn how to customize PiSloth's step.


**Run the Code**

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 custom_step.py

After the code runs, press the **key ZX** and **key NM** (according to the actual code) to make PiSloth do the step shown in the figure, and you can also let it do other steps.

.. image:: ezblock/img/diy_pic.jpg
  :width: 400
  :align: center

Press the **key SPACE** to print the angle of the 4 servos at this time. You need to record these angle values, which will be used in the next project :ref:`Custom Action`.

.. image:: img/custom_step.png
  :width: 400
  :align: center

**Code**

.. code-block:: python

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

    right_leg_servo = Servo(PWM('P0'))
    right_foot_servo = Servo(PWM('P1'))
    left_leg_servo = Servo(PWM('P2'))
    left_foot_servo = Servo(PWM('P3'))


    def readchar():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    manual = '''
    Press keys on keyboard to control PiSloth!
        Q: Increase the servo angle of the left leg
        W: Decrease the servo angle of the left leg
        Z: Increase the servo angle of the left foot 
        X: Decrease the servo angle of the left foot
        I: Increase the servo angle of the right leg
        O: Decrease the servo angle of the right leg
        N: Increase the servo angle of the right foot
        M: Decrease the servo angle of the right foot   
        SPACE: Print all angle
        ESC: Quit
    '''

    def main():
        print(manual)
            
        left_leg=0
        left_foot=0
        right_leg=0
        right_foot=0
        while True:
            key = readchar()
            # print(key)
            if key == "q":
                left_leg = left_leg+5
            elif key == "w":
                left_leg = left_leg-5
            elif key == "z":
                left_foot = left_foot+5
            elif key == "x":
                left_foot = left_foot-5
            elif key == "i":
                right_leg = right_leg+5
            elif key == "o":
                right_leg = right_leg-5
            elif key == "n":
                right_foot = right_foot+5
            elif key == "m":
                right_foot = right_foot-5
            elif key == chr(32): # 32 for space
                print(right_leg,right_foot,left_leg,left_foot)
            elif key == chr(27): # 27 for ESC
                break

            right_leg_servo.angle(right_leg) 
            right_foot_servo.angle(right_foot) 
            left_leg_servo.angle(left_leg) 
            left_foot_servo.angle(left_foot) 
            # time.sleep(0.05)

        print("\nQuit")

    if __name__ == "__main__":
        main()   
