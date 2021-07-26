Remote Control
==================

In this project, we will learn how to use the keyboard to remotely control the Pisloth. You can control the Pisloth to move up, down, left, and right and speak through specific keys.
**Code**

.. code:: python

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

        W: Forward
        A: Turn left
        S: Backward
        D: Turn right
        1: Sound effect: talk1
        2: Sound effect: talk2
        3: Sound effect: talk3
        4: Sound effect: depress2
        Q: Say: "Oh hello there"
        E: Say: "bye"
        ESC: Quit
    '''

    def main():
        print(manual)
        while True:
            key = readkey()
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

This function refers to the standard input stream and returns the first character of the data stream read. ``tty.setraw(sys.stdin.fileno)`` is to change the standard input stream to raw mode, that is, all characters 
will not be escaped during transmission, including special characters. Before changing the mode, back up the original mode, and restore it after the change. ``old_settings = termios.tcgetattr(fd)'' and
``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)'' plays the role of backup and restore.
.. code:: python

    def readchar():
		fd = sys.stdin.fileno() 
		old_settings = termios.tcgetattr(fd) 
		try:
			tty.setraw(sys.stdin.fileno())  
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  
		return ch


Finally, according to reading the pressed keyboard character, let Pisloth do the actions we set, call the function of tts to speak or play the audio file prepared in advance

.. code:: python

    key = readkey()
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