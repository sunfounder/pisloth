Obstacle Avoidance
=====================

In this project, Pisloth will use an ultrasonic module to detect obstacles in front. When an obstacle is detected, Pisloth will be taken aback, and then find another way to move on.

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

Read the distance detected by the ultrasonic, set the condition to judge, when the distance is less than ``alert_distance``, play the audio file ``sign.wav``
and let Pisloth do the ``hook``, ``stand``, ``turn left``, ``stand`` actions in sequence. When the distance is greater than ``alert_distance``,
Pisloth does the ``forward`` action.

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


