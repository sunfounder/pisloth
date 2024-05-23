.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Don't Touch Me
==================

If you don't meet PiSloth's needs, it will get angry and stay away from your touch.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pisloth/examples
    sudo python3 dont_touch_me.py


**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

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

**How it works?**

Instantiate various classes of ``Music``, ``Sloth`` and ``Ultrasonic`` to be used.

.. code-block:: python

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])
    sonar = Ultrasonic(Pin("D2") ,Pin("D3"))

Here is the main program.

* Read the ``distance`` detected by the ultrasonic module and print it.
* When the ``distance`` is less than or equal to ``alert_distance`` (the threshold value set earlier, which is 20), play the sound effect ``talk3.wav`` and move ``backward``.
* When the ``distance`` is greater than ``alert_distance``, PiSloth will Stand.

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
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla_software`.