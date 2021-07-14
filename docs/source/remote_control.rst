Remote Control
==================

在这个项目中，我们会学习如何用键盘远程控制pisloth。你可以通过特定的键位来操控pisloth上下左右移动和讲话。

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

该函数会引用标准输入流，将读取到的数据流的第一个字符返回。 ``tty.setraw(sys.stdin.fileno)`` 是将标准输入流改为raw模式，即所有字符在
传输过程中都不会被转义，包括特殊字符。更改模式之前要备份原来的模式，更改之后要还原回来， ``old_settings = termios.tcgetattr(fd)`` 与
``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` 就起到了备份和还原的作用。

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


最后根据读取到按下的键盘字符让Pisloth做出设定好的动作，调用tts的功能讲话或者播放提前准备好的音频文件

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