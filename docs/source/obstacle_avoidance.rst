Obstacle Avoidance
=====================

In this project, Pisloth will use an ultrasonic module to detect obstacles in front. When PiSloth detects an obstacle, it will send a signal and look for another direction to move forward.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 avoid.py

After the code runs, PiSloth will walk forward. If it detects that the distance of the obstacle ahead is less than 10cm, it will stop and sound a warning, then turn left and stop. If there is no obstacle in the direction after turning left or the obstacle distance is greater than 10, it will continue to move forward.


**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

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


**How it works?**

You can get the distance by importing the ``Ultrasonic`` class.

.. code-block:: python

    from robot_hat import Ultrasonic

Then initialize the ultrasonic pins.

.. code-block:: python

    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

Here is the main program.

* Read the ``distance`` detected by ultrasonic module and filter out the values less than 0 (When the ultrasonic module is too far from the obstacle or cannot read the data correctly, ``distance<0`` will appear).
* When the ``distance`` is less than or equal to  ``alert_distance`` (the threshold value set earlier, which is 10), play the sound effect ``sign.wav``. PiSloth does ``hook``, ``stand``, ``left turn`` and ``stand`` in sequence.
* When the ``distance`` is greater than ``alert_distance``, PiSloth will move ``forward``.

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
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.