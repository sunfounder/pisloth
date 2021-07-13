Obstacle Avoidance
=====================

在这个项目中，pisloth将使用超声波模块检测前面的障碍物。当检测到障碍物时，pisloth会吓一跳，然后连忙后退并寻找别的路继续前行。

**Code**

.. code:: python

    from pisloth import Sloth
    from robot_hat import TTS, Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time
    import os

    tts = TTS()
    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

    alert_distance = 10

    def main():
        distance = sonar.read()
        if distance < 0:
            pass
        elif distance <= alert_distance:
            try:
                music.sound_effect_threading('./sounds/sign.wav')
            except Exception as e:
                print(e)
            sloth.do_action('hook', 1,95)
            sloth.do_action('stand', 1,95)
            time.sleep(0.2)
            sloth.do_action('turn left',7,95)
            sloth.do_action('stand', 1,95)
            time.sleep(0.2)
        else :
            sloth.do_action('forward', 1,95)


    if __name__ == "__main__":
        while True:
            main()  

**How it works?**

You can get the distance only by calling the Ultrasonic library.

.. code:: python

    from robot_hat import Ultrasonic

Then initialize the ultrasonic pins.

.. code:: python

    sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

读取超声波检测距离值，设置条件判断，当距离小于 ``alert_distance`` 时，播放音频文件
并让pisloth依次做 ``hook`` , ``stand`` , ``turn left`` , ``stand`` 动作。当距离大于 ``alert_distance`` 时，
pisloth做 ``forward`` 动作。

.. code:: python

    distance = sonar.read()
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1,95)
        sloth.do_action('stand', 1,95)
        time.sleep(0.2)
        sloth.do_action('turn left',7,95)
        sloth.do_action('stand', 1,95)
        time.sleep(0.2)
    else :
        sloth.do_action('forward', 1,95)


