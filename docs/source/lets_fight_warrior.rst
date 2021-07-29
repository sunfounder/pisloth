Let\'s fight! Warrior!
=======================

In this project, we will make Pisloth a warrior who will provoke you, and it will rush towards you full of fighting spirit.

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


    if __name__ == "__main__":
        while True:
            main()

**How it works?**

The ultrasonic module reads the distance between the obstacle and the Pisloth, when the distance is less than or equal to alert_distance and
When greater than or equal to ``contact_distance``, Pisloth will play ``warning.wav`` and ``attack.mp3``, and let him cycle forward to charge, when the distance is less than or equal to ``contact_distance``, it will jump out of the loop and stop charging.

.. code:: python

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
    When the ultrasonic module is too far away from the obstacle or the data is not read due to the wire problem, the situation of ``distance<0`` will appear, you can use it ``continue`` ignore these disturbances and continue the cycle.