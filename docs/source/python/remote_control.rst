Remote Control
==================

In this project, we will learn how to use the keyboard to remotely control the PiSloth. You can control the PiSloth to move up, down, left, and right and speak through specific keys.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 keyboard_control.py

Once the code runs, you can control PiSloth by pressing ``wasd``, play different sound effects by pressing ``1234``, and make PiSloth talk by pressing ``qe``.

Press ``esc`` to exit.

* w: Go Forward
* a: Turn Left
* s: Backward
* d: Turn Right
* 1: Sound effect: talk1
* 2: Sound effect: talk2
* 3: Sound effect: talk3
* 4: Sound effect: depress2
* q: Say: "Oh hello there"
* e: Say: "bye"
* esc: Quit

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pisloth import Sloth
    from robot_hat import Music
    from robot_hat import TTS
    import sys
    import tty
    import termios
    import time

    sloth = Sloth([1,2,3,4])
    tts = TTS()
    music = Music()
    sloth.set_offset([0,0,0,0])

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

        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        1: Sound effect: talk1
        2: Sound effect: talk2
        3: Sound effect: talk3
        4: Sound effect: depress2
        q: Say: "Oh hello there"
        e: Say: "bye"
        esc: Quit
    '''

    def main():
        print(manual)
        while True:
            key = readchar().lower()
            # print(key)
            if key == "w":
                sloth.do_action('forward', 1, 90)
            elif key == "a":
                sloth.do_action('turn left', 1, 90)
            elif key == "s":
                sloth.do_action('backward', 1, 90)
            elif key == "d":
                sloth.do_action('turn right', 1, 90)
            elif key == "1":
                music.sound_effect_play('./sounds/talk1.wav')
            elif key == "2":
                music.sound_effect_play('./sounds/talk2.wav')
            elif key == "3":
                music.sound_effect_play('./sounds/talk3.wav')
            elif key == "4":
                music.sound_effect_play('./sounds/depress.wav')
            elif key == "q":
                tts.say("Oh hello there")
            elif key == "e":
                tts.say("bye")
            elif key == chr(27): # 27 for ESC
                break
            time.sleep(0.05)
        print("\nQuit")

    if __name__ == "__main__":
        main() 

**How it works?**

This function refers to the standard input stream and returns the first character of the data stream read. 

* ``tty.setraw(sys.stdin.fileno)`` is to change the standard input stream to raw mode, that is, all characters will not be escaped during transmission, including special characters. Before changing the mode, back up the original mode, and restore it after the change. 
* ``old_settings = termios.tcgetattr(fd)`` and ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` plays the role of backup and restore.


.. code-block:: python

    def readchar():
		fd = sys.stdin.fileno() 
		old_settings = termios.tcgetattr(fd) 
		try:
			tty.setraw(sys.stdin.fileno())  
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  
		return ch



Finally, according to the read keyboard characters, let PiSloth do the actions we set, call the ``tts.say()`` function to speak or play the sound effects prepared in advance.

.. code-block:: python

    key = readchar().lower()
        # print(key)
        if key == "w":
            sloth.do_action('forward', 1, 90)
        elif key == "a":
            sloth.do_action('turn left', 1, 90)
        elif key == "s":
            sloth.do_action('backward', 1, 90)
        elif key == "d":
            sloth.do_action('turn right', 1, 90)
        elif key == "1":
            music.sound_effect_play('./sounds/talk1.wav')
        elif key == "2":
            music.sound_effect_play('./sounds/talk2.wav')
        elif key == "3":
            music.sound_effect_play('./sounds/talk3.wav')
        elif key == "4":
            music.sound_effect_play('./sounds/depress.wav')
        elif key == "q":
            tts.say("Oh hello there")
        elif key == "e":
            tts.say("bye")
        elif key == chr(27): # 27 for ESC
            break



.. note::
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla_software`.