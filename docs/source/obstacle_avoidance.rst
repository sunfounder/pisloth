避障
=====================

在这个项目中，PiSloth 将使用超声波模块来检测前方的障碍物。
当 PiSloth 检测到障碍物时，它会发出信号并寻找另一个方向前进。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 avoid.py

代码运行后，PiSloth 会向前走。如果检测到前方障碍物的距离小于10cm，就会停车并发出警告，然后左转停车。
如果左转后方向没有障碍物或障碍物距离大于10，则继续向前移动。

**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python


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
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

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
            time.sleep(0.5)
            sloth.do_action('stand', 1,95)
            time.sleep(0.5)
            sloth.do_action('turn left',7,90)
            sloth.do_action('stand', 1,95)
            time.sleep(0.2)
        else :
            sloth.do_action('forward', 1,90)


    if __name__ == "__main__":
        while True:
            main()


**这个怎么运作？**

您可以通过导入 ``Ultrasonic`` 类来实现距离检测。

.. code-block:: python

    from robot_hat import Ultrasonic

然后初始化超声波引脚。

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

这里是主程序。

* 读取超声波模块检测到的 ``distance`` (距离)，过滤掉小于0的值（当超声波模块距离障碍物太远或无法正确读取数据时，会出现“距离<0”）。
* 当 ``distance`` 小于等于 ``alert_distance`` （之前设置的阈值，即10）时，播放音效 ``sign.wav``。 PiSloth 依次做 ``hook`` (勾脚), ``stand`` (站立), ``left turn`` (左转) 和 ``stand`` (右转)。
* 当 ``distance`` 大于 ``alert_distance`` 时，PiSloth 会向前移动。

.. code-block:: python

    distance = sonar.read()
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1,95)
        time.sleep(0.5)
        sloth.do_action('stand', 1,95)
        time.sleep(0.5)
        sloth.do_action('turn left',7,90)
        sloth.do_action('stand', 1,95)
        time.sleep(0.2)
    else :
        sloth.do_action('forward', 1,90)


.. note::
    
    您可以通过 :ref:`Filezilla Software` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。