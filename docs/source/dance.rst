
.. _dance_python:

Dance
=========

Now, PiSltoh will show you his newly learned dance.

.. image:: ezblock/img/dance_pic.jpg
    :width: 400
    :align: center

.. note::

    You can download and print the :download:`cardstock <https://github.com/sunfounder/sf-pdf/tree/master/assembly_file/card>` for your PiSloth.

**Run the Code**


.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 dancing.py

The whole dance is divided into 2 parts, and PiSloth will finish these 2 parts with the music. If you don't stop the code, it will repeat the dance.


**Code**

.. note::

    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to a specific path like ``/home/pi/pisloth/examples``. After modifying the code, you can run it directly to see the effect. After confirming that there are no problems, you can use the Copy button to copy the modified code, then open the source code in Terminal via ``nano dancing.py`` and paste it.


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


    def main():
    
        music.background_music('./musics/india-Arulo.mp3')
        music.music_set_volume(20)
        sloth.do_action('stomp left',3,bpm=129)
        sloth.do_action('stomp right',3,bpm=129)
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

You can make PiSloth play music by importing the following libraries.

.. code-block:: python

    from robot_hat import TTS, Music

Play the background music in the ``pisloth/examples/musics`` directory and set the volume to 20. You can also add music to the ``musics`` folder via :ref:`Filezilla Software`.

.. code-block:: python

    music.background_music('./musics/india-Arulo.mp3')
    music.music_set_volume(20)

In general, all actions of PiSloth can be implemented with the ``sloth.do_action()`` function. It has four parameters:

* ``motion_name`` is the name of specific actions, including: ``forward``, ``turn right``, ``turn left``, ``backward``, ``stand``, ``moon walk left``, ``moon walk right``, ``hook``, ``big swing``, ``swing``, ``walk boldly``, ``walk backward boldly``, ``walk shyly``, ``walk backward shyly``, ``stomp rihgt``, ``stomp left``, ``close``, ``open``, ``tiptoe left``, ``tiptoe right``, ``fall left``, ``fall right``.
* ``step`` represents the number of each action is done, the default is 1.
* ``speed`` indicates the speed of the action, the default is 50 and the range is 0~100.
* ``bpm`` means rhythm, the bpm parameter here affects the interval time of Pisloth movement. The higher the value, the shorter the interval time. When we know the beat of a song through the **bpm calculator**, we can make PiSloth dance to the music.


For music bmp, if you want to know more, you can refer to:
https://en.wikipedia.org/wiki/Tempo

.. note::
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`Filezilla Software`.