Move
========

The basic functions of Pisloth have been encapsulated in ``sloth.py`` under the path ``/home/pi/pisloth``, chiefly controlling the servo.

Let the Pisloth move forward, left and right, which requires us to use commands to drive the four servos on the Pisloth leg.

You can open ``move.py`` in the folder of the ``example`` with command ``sudo pyrhon3 move.py`` or directly copy the following code to the Python IDE to run.

**Code**

.. code:: Python

    from pisloth import Sloth

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

    def main():
        sloth.do_action('turn left', 7, 90)
        sloth.do_action('forward', 5, 90)
        sloth.do_action('turn right', 7, 90)
        sloth.do_action('forward', 5, 90)


    if __name__ == ``__main__``:
        while True:
            main()

**How it works?**

First, import the libraries to support the basic functionality of pisloth.

.. code:: python

    from pisloth import Sloth


Then instantiate the Pisloth class.

.. code:: python

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

Finally use the following function to make Pisloth move.

.. code:: python

    sloth.do_action('turn left', 7, 90)
    sloth.do_action('forward', 5, 90)
    sloth.do_action('turn right', 7, 90)
    sloth.do_action('forward', 5, 90)

In general, all actions of PiSloth can be implemented with the function ``sloth.do_action(motion_name,step=1,speed=None,bpm=None)''. It has four parameters:

* ``motion_name``  is the preset specific actions, including: ``forward`` , ``turn right`` , ``turn left`` , ``backward`` , ``stand`` , ``moon walk left`` , ``moon walk right`` , ``hook`` , ``big swing`` , ``swing`` , ``walk boldly`` , ``walk backward boldly`` , ``walk shyly`` , ``walk backward shyly`` , ``stomp rihgt`` , ``stomp left`` , ``close`` , ``open`` , ``tiptoe left`` , ``tiptoe right`` , ``fall left`` , ``fall right``

* ``step`` represents the number of actions, the default number is 1.

* ``speed`` means the speed of the action, the default is 50, the range is 0~100.

* ``bpm`` means rhythm, we will use it later in the dance course.
