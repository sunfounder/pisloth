Let\'s fight! Warrior!
=======================

在这个项目中，我们会让Pisloth变成一位会挑衅你的战士，它会浑身充满着斗志向你冲过来。

**Code**

.. code:: python

    from pisloth import Sloth
    from robot_hat import Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time
    import os


    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

    alert_distance = 40
    contact_distance = 5

    def main():
        distance = sonar.read()
        if distance <= alert_distance and distance >= contact_distance :
            try:
                music.sound_effect_threading('./sounds/warning.wav')
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


    if __name__ == "__main__":
        while True:
            main()

**How it works?**

红外感应模块读取障碍物与pisloth的距离，当这个距离小于或等于alert_distance并
大于或等于 ``contact_distance`` 时，pisloth会播放 ``warning.wav`` ，并让pisloth循环执行
向前冲锋的动作，当距离小于或等于 ``contact_distance`` 时便跳出循环停止冲锋。

.. code:: python

    distance = sonar.read()
    if distance <= alert_distance and distance >= contact_distance :
        try:
            music.sound_effect_threading('./sounds/warning.wav')
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
    当红外感应模块距离障碍过远或者由于线路问题导致没有读到数据时会出现 ``distance<0`` 的情况，可以用
     ``continue`` 忽略这些干扰继续循环。