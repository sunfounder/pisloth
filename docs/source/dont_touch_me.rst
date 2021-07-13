Don\'t Touch Me
==================

在这个项目中，我们会让Pisloth表达自己的小情绪，当你试着触摸Pisloth时，它会生气的说不要碰我，然后退后离开你。

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

**How it works?**

实例化各种要用到的音乐类、pisloth以及红外感应模块的类

.. code:: python

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

红外感应模块读取你的手与pisloth的距离，设置判断条件，当这个距离小于或等于alert_distance时，pisloth会播放音频文件并做出backward和stand动作。

.. code:: python

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