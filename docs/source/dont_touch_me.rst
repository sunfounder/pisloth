Don\'t Touch Me
==================

In this project, we will let Pisloth express his little emotions. When you try to touch Pisloth, He will be on his guard and get back from you.

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

Instantiate various classes of music, pislot and infrared sensor modules to be used.

.. code:: python

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

The ultrasonic module reads the distance between your hand and the Pisloth and sets the judgment condition. When the distance is less than or equal to alert_distance, Pisloth will play the audio file and do ``backward`` and ``stand`` actions.

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