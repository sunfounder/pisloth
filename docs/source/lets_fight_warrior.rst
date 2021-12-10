战斗吧！战士！
=======================

在这里，PiSloth 是一个勇敢的战士，当它出现在敌人面前时，它会发出咆哮冲向敌人。

.. image:: ezblock/media/warrir.jpg
  :width: 400
  :align: center

.. note::

    您可以为您的 PiSloth 下载并打印卡通面具。
    
    .. `PDF Cartoon Mask <https://github.com/sunfounder/sf-pdf/tree/master/prop_card/cartoon_mask>`_ for your PiSloth.

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 lets_fight.py

代码运行后，PiSloth会不断检测障碍物的距离，当距离在5到40之间时，PiSloth会发出轰鸣声并向前冲去；当障碍物的距离小于 5 时，PiSloth 将停止。



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

    alert_distance = 40
    contact_distance = 5

    def main():
        distance = sonar.read()
        if distance <= alert_distance and distance >= contact_distance :
            try:
                music.sound_effect_play('./sounds/battle.wav')
                music.background_music('./musics/attack.mp3')
                music.music_set_volume(20)
            except Exception as e:
                print(e)
            while True:
                distance = sonar.read()
                print(distance)
                if distance < 0:
                    continue
                if distance <= contact_distance:
                    break
                sloth.do_action('forward', 1,90)
        sloth.do_action('stand', 1, 90)
        time.sleep(1)


    if __name__ == "__main__":
        while True:
            main()



**这个怎么运作？**

这里是主程序。

* 读取 ``distance`` 超声波模块检测到的值，过滤掉小于0的值（当超声波模块距离障碍物太远或无法正确读取数据时， distance将会是一个小于0的无效值）。
* 当 ``distance`` 在5和40之间，PiSloth将发出 ``warning.wav`` 和 ``attack.mp3`` 音效并向前移动。
* 当 ``distance`` 小于 5 时，PiSloth 将保持 ``stand`` 位置。


.. code-block:: python

    distance = sonar.read()
    if distance <= alert_distance and distance >= contact_distance :
        try:
            music.sound_effect_play('./sounds/battle.wav')
            music.background_music('./musics/attack.mp3')
            music.music_set_volume(20)
        except Exception as e:
            print(e)
        while True:
            distance = sonar.read()
            print(distance)
            if distance< 0:
                continue
            if distance<=contact_distance:
                break
            sloth.do_action('forward', 1,95)
    sloth.do_action('stand', 1, 90)
    time.sleep(1)


.. note::
    
    您可以通过 :ref:`Filezilla Software` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。