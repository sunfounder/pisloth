Emotional PiSloth
=======================

在这个项目，我们会让pisloth变得更加生动，我们会让它表现出更多人类的感情动作，
当然学完这课后，你也可以自己设计更多的感情动作出来。

**Code**

.. code:: python

    from pisloth import Sloth
    from robot_hat import Music
    import time

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

    def confuse():
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 100)  

    def happy():
        try:
            music.sound_effect_threading('./sounds/happy2.wav')
        except Exception as e:
            print(e)
        for i in range(3):
            sloth.do_action('hook', 1, 100)
            sloth.do_action('stand', 1, 100)

    def fear():
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 100)
        sloth.do_action('stand', 1, 100)
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 100)
        sloth.do_action('stand', 1, 100)

    def sad():
        try:
            music.sound_effect_threading('./sounds/depress.wav')
        except Exception as e:
            print(e)
        sloth.do_action('big swing', 1, 100)  

    def angry():
        try:
            music.sound_effect_threading('./sounds/error.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 100)  
        sloth.do_action('stand', 1, 100)

    def fail():
        try:
            music.sound_effect_threading('./sounds/depress2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('fall left', 1, 100)  

    def shy():
        try:
            music.sound_effect_threading('./sounds/talk3.wav')
        except Exception as e:
            print(e)
        sloth.do_action('close', 1, 100)  
        time.sleep(1)    
        try:
            music.sound_effect_threading('./sounds/talk2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('stand', 1, 100)    

    def main():

        print("shy")
        shy()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("confuse")
        confuse()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("happy")
        happy()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("fear")
        fear()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("sad")
        sad()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("angry")
        angry()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)

        print("fail")
        fail()
        time.sleep(1)
        sloth.do_action('stand', 1, 100)
        time.sleep(2)       


    if __name__ == "__main__":
        while True:
            main()

**How it works?**

Pisloth播放sign.wav并执行 ``hook`` 动作表示confuse.

.. code:: python

    def confuse():
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 100)  

Pisloth播放happy2.wav并循环3次执行 ``hook`` 和 ``stand``  动作表示happy.

.. code:: python

    def happy():
        try:
            music.sound_effect_threading('./sounds/happy2.wav')
        except Exception as e:
            print(e)
        for i in range(3):
            sloth.do_action('hook', 1, 100)
            sloth.do_action('stand', 1, 100)

Pisloth播放warning.wav并执行 ``hook`` , ``stand`` , ``walk backward boldly`` 动作表示fear.

.. code:: python

    def fear():
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 100)
        sloth.do_action('stand', 1, 100)
        try:
            music.sound_effect_threading('./sounds/warning.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 100)
        sloth.do_action('stand', 1, 100)

Pisloth播放depress.wav并执行 ``big swing`` 动作表示sad.

.. code:: python

    def sad():
        try:
            music.sound_effect_threading('./sounds/depress.wav')
        except Exception as e:
            print(e)
        sloth.do_action('big swing', 1, 100)  

Pisloth播放error.wav并执行 ``walk backward boldly`` 和 ``stand`` 动作表示angry.

.. code:: python

    def angry():
        try:
            music.sound_effect_threading('./sounds/error.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 100)  
        sloth.do_action('stand', 1, 100)

Pisloth播放depress2.wav并执行 ``fall left`` 动作表示fail.

.. code:: python

    def fail():
        try:
            music.sound_effect_threading('./sounds/depress2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('fall left', 1, 100)  

.. note::
    这个动作会让pisloth摔倒，注意别让它从桌子上落下摔坏。

Pisloth播放talk3.wav,talk2.wav并执行 ``close`` , ``stand`` 动作表示shy.

.. code:: python

    def shy():
        try:
            music.sound_effect_threading('./sounds/talk3.wav')
        except Exception as e:
            print(e)
        sloth.do_action('close', 1, 100)  
        time.sleep(1)    
        try:
            music.sound_effect_threading('./sounds/talk2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('stand', 1, 100) 