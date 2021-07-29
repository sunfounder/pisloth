Emotional PiSloth
=======================

In this project, we will make the Pisloth more vivid, and we will make it show more human emotions,
of course, after learning this lesson, you can also design more emotional actions yourself.

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

Pisloth plays ``sign.wav`` and executes the ``hook'' action to indicate confuse.

.. code:: python

    def confuse():
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1, 100)  

Pisloth plays ``happy2.wav`` and executes the ``hook`` and ``stand'' actions 3 times to indicate happy.

.. code:: python

    def happy():
        try:
            music.sound_effect_threading('./sounds/happy2.wav')
        except Exception as e:
            print(e)
        for i in range(3):
            sloth.do_action('hook', 1, 100)
            sloth.do_action('stand', 1, 100)

Pisloth plays warning.wav and executes ``hook``, ``stand``, ``walk backward boldly`` actions to indicate fear.

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

Pisloth plays ``depress.wav`` and performs the ``big swing'' action to indicate sad.

.. code:: python

    def sad():
        try:
            music.sound_effect_threading('./sounds/depress.wav')
        except Exception as e:
            print(e)
        sloth.do_action('big swing', 1, 100)  

Pisloth plays ``error.wav`` and performs the ``walk backward boldly`` and ``stand`` actions to indicate angry.

.. code:: python

    def angry():
        try:
            music.sound_effect_threading('./sounds/error.wav')
        except Exception as e:
            print(e)
        sloth.do_action('walk backward boldly', 1, 100)  
        sloth.do_action('stand', 1, 100)

Pisloth plays ``depress2.wav`` and executes the ``fall left`` action to indicate a fall.

.. code:: python

    def fail():
        try:
            music.sound_effect_threading('./sounds/depress2.wav')
        except Exception as e:
            print(e)
        sloth.do_action('fall left', 1, 100)  

.. note::
    This action will make the Pisloth fall, be careful not to let it fall off the table and break it.


Pisloth plays ``talk3.wav``, ``talk2.wav`` and executes ``close``, ``stand'' action means shy.

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