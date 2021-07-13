Move
========

The basic functions of Pisloth have been encapsulated in ``sloth.py`` under the path ``/home/pi/pisloth``, chiefly controlling the servo.

让pisloth向前、向左、向右移动，这需要我们用命令来驱动pisloth腿上的四个舵机。

You can open ``move.py`` in the folder of the ``example`` or directly copy the following code to the Python IDE to run.

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


然后实例化pisloth的类

.. code:: python

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

Finally use the following function to make Pisloth move.

.. code:: python

    sloth.do_action('turn left', 7, 90)
    sloth.do_action('forward', 5, 90)
    sloth.do_action('turn right', 7, 90)
    sloth.do_action('forward', 5, 90)

总的来说，PiSloth的所有行动都可以用函数 ``sloth.do_action(motion_name,step=1,speed=None,bpm=None)`` 来实现。它拥有四个参数：

* ``motion_name`` 是调用预设好的具体动作，包括： ``forward`` , ``turn right`` , ``turn left`` , ``backward`` , ``stand`` , ``moon walk left`` , ``moon walk right`` , ``hook`` , ``big swing`` , ``swing`` , ``walk boldly`` , ``walk backward boldly`` , ``walk shyly`` , ``walk backward shyly`` , ``stomp rihgt`` , ``stomp left`` , ``close`` , ``open`` , ``tiptoe left`` , ``tiptoe right`` , ``fall left`` , ``fall right``

* ``step`` 表示动作的次数，默认次数是1

* ``speed`` 表示做动作的速度，默认是50，范围是0~100

* ``bpm`` 表示节奏，我们在后面的dance课程会有用到
