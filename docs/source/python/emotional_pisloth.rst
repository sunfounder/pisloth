情绪丰富的 PiSloth
=======================

PiSloth 拥有非常多的情绪。时而快乐，时而害羞，时而迷茫。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 emotional_pisloth.py


**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python


    from pisloth import Sloth
    from robot_hat import TTS, Music
    import time

    tts = TTS()
    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

    def confuse():
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 90)  

    def happy():
        try:
            music.sound_effect_threading('./sounds/happy2.wav')
        except Exception as e:
            print(e)
        for i in range(3):
            sloth.do_action('hook', 1, 90)
            sloth.do_action('stand', 1, 90)

    def fear():
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 90)
        sloth.do_action('stand', 1, 90)
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 90)
        sloth.do_action('stand', 1, 90)

    def sad():
        try:
            music.sound_effect_threading('./sounds/depress.wav')
        except Exception as e:
            print(e)
        sloth.do_action('big swing', 1, 90)  

    def angry():
        try:
            music.sound_effect_threading('./sounds/error.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 90)  
        sloth.do_action('stand', 1, 90)

    def fail():
        try:
            music.sound_effect_threading('./sounds/depress2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('fall left', 1, 90)  

    def shy():
        try:
            music.sound_effect_threading('./sounds/talk3.wav')
        except Exception as e:
            print(e)
        sloth.do_action('close', 1, 90)  
        time.sleep(1)    
        try:
            music.sound_effect_threading('./sounds/talk2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('stand', 1, 90)    

    def main():

        print("shy")
        shy()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("confuse")
        confuse()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("happy")
        happy()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("fear")
        fear()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("sad")
        sad()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("angry")
        angry()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)

        print("fail")
        fail()
        time.sleep(1)
        sloth.do_action('stand', 1, 90)
        time.sleep(2)       


    if __name__ == "__main__":
        while True:
            main()

**这个怎么运作？**

在这个项目中，动作+音效组合成不同的情感动作，你也可以自己修改。

.. note::

    这个 ``fail`` 动作会使 PiSloth 摔倒，注意不要让它从桌子上掉下来弄坏它。

    您可以通过 :ref:`filezilla` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。