遥控
==================

在这个项目中，我们将学习如何使用键盘远程控制 PiSloth。 您可以控制 PiSloth 上下左右移动并通过特定键说话。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 keyboard_control.py



**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

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
            key = readchar()
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

**这个怎么运作？**

该功能引用标准输入流并返回读取的数据流的第一个字符。

* ``tty.setraw(sys.stdin.fileno)`` 就是将标准输入流改为raw模式，即传输过程中所有字符都不会被转义，包括特殊字符。
* ``old_settings = termios.tcgetattr(fd)`` 和 ``termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)`` 并起到备份和恢复的作用。


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



最后，根据读取的键盘字符，让PiSloth做我们设置的动作，调用 ``tts.say()`` 函数说话或播放事先准备好的音效。

.. code-block:: python

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



.. note::
    
    您可以通过 :ref:`Filezilla Software` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。