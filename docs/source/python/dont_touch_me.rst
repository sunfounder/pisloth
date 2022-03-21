别碰我
==================

如果它看到你伸手想去摸它，它会生气并离你远远的。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 dont_touch_me.py


**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pisloth import Sloth
    from robot_hat import Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time
    import os


    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

    alert_distance = 20

    def main():
        distance = sonar.read()
        print(distance)
        if distance <= alert_distance :
            try:
                music.sound_effect_threading('./sounds/talk3.wav')
            except Exception as e:
                print(e)
            sloth.do_action('backward', 2, 90)
        else:
            sloth.do_action('stand', 1, 90)
            time.sleep(1)


    if __name__ == "__main__":
        while True:
            main() 

**这个怎么运作？**

实例化 ``Music``, ``Sloth`` 和 ``Ultrasonic`` 以供使用。


.. code-block:: python

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

这里是主程序。


* 读取超声波模块检测到的数据 ``distance`` 并打印出来。
* 当 ``distance`` 小于或等于 ``alert_distance`` （之前设置的阈值，即 20）时，播放音效 ``talk3.wav`` 并向后移动。
* 当 ``distance`` 大于 ``alert_distance`` 时，PiSloth 将站立。


.. code-block:: python

    distance = sonar.read()
    print(distance)
    if distance <= alert_distance :
        try:
            music.sound_effect_threading('./sounds/talk3.wav')
        except Exception as e:
            print(e)
        sloth.do_action('backward', 2, 90)
    else:
        sloth.do_action('stand', 1, 90)
        time.sleep(1)


.. note::
    
    您可以通过 :ref:`filezilla` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。