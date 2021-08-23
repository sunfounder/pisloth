Let's Fight! Warrior!
=======================

Here, PiSloth is a brave warrior, when it appears in front of the enemy, it will let out a roar and rush to the enemy.

.. image:: ezblock/media/warrir.jpg
  :width: 400
  :align: center

.. note::

    You can download and print the `cardstock <https://github.com/sunfounder/sf-pdf/tree/master/prop_card/cartoon_mask>`_ for your PiSloth.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 lets_fight.py

After the code is run, PiSloth will continuously detect the distance of the obstacle, when the distance is between 5 and 40, PiSloth will make a roaring sound and rush forward; when the distance of the obstacle is less than 5, PiSloth will stop.



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



**How it works?**

Here is the main program.

* Read the ``distance`` detected by ultrasonic module and filter out the values less than 0 (When the ultrasonic module is too far from the obstacle or cannot read the data correctly, ``distance<0`` will appear).
* When the ``distance`` is between 5 and 40, PiSloth will play ``warning.wav`` and ``attack.mp3`` and move ``forward``.
* When the ``distance`` is less than 5, PiSloth will keep the ``stand`` position.


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
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.