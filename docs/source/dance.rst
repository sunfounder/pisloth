Dance
=========

In this project, we will play a piece of music and let Pisloth dance to the rhythm of the music.

You can open ``dancing.py`` in the folder of the ``example`` with command ``sudo pyrhon3 dancing.py`` or directly copy the following code to the Python IDE to run.

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

    def main():
    
        music.background_music('./musics/india-Arulo.mp3')
        music.music_set_volume(20)
        sloth.do_action('stomp left',3,bpm=129)
        sloth.do_action('stomp rihgt',3,bpm=129)
        sloth.do_action('moon walk left',3,bpm=129)
        sloth.do_action('moon walk right',3,bpm=129)
        for i in range(3):
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        for i in range(3):
            sloth.do_action('close',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
            sloth.do_action('open',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        sloth.do_action('tiptoe left',2,bpm=129)
        sloth.do_action('tiptoe right',2,bpm=129)

        sloth.do_action('stomp left',3,bpm=129)
        sloth.do_action('stomp rihgt',3,bpm=129)
        sloth.do_action('moon walk left',3,bpm=129)
        sloth.do_action('moon walk right',3,bpm=129)
        for i in range(3):
            sloth.do_action('hook',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        for i in range(4):
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('big swing',1,bpm=129)
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)

        sloth.do_action('tiptoe right',2,bpm=129)
        sloth.do_action('stand',2,bpm=129)

    

        music.music_stop()
        time.sleep(10)



    if __name__ == "__main__":
        while True:
            main()

**How it works?**

You can make Pisloth play music by importing the following library.

.. code:: python

    from robot_hat import TTS, Music

Play the background music in the music directory and set the volume to 20.

.. code:: python

    music.background_music('./musics/india-Arulo.mp3')
    music.music_set_volume(20)

Execute the function ``sloth.do_action(motion_name,step=1,speed=None,bpm=None)`` to let Pisloth perform the actions we set.
The bpm parameter here will affect the interval time between Pisloth's actions, the larger the value, the shorter the interval time.
When we learn about the bpm of a piece of music through some methods, you can freely match the movement of the Pisloth according to the bpm of this music to make it dance with different styles of music.

For music bmp, if you want to know more, you can refer to:
https://en.wikipedia.org/wiki/Tempo