Move
========

This is the first project. PiSloth has woken up, and it moves freely.

.. image:: img/movement.png
  :align: center


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/pisloth/examples
    sudo python3 move.py

After running the code, you will see PiSloth move left 7 steps, forward 5 steps, right 7 steps, and forward 5 steps.


**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pisloth import Sloth

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

    def main():
        sloth.do_action('turn left', 7, 90)
        sloth.do_action('forward', 5, 90)
        sloth.do_action('turn right', 7, 90)
        sloth.do_action('forward', 5, 90)


    if __name__ == "__main__":
        while True:
            main()

**How it works?**

First, import the ``Sloth`` class from the ``pisloth`` library you have installed, which contains all of PiSloth's actions and the functions that implement them.

.. code-block:: python

    from pisloth import Sloth


Then instantiate the ``Sloth`` class.

.. code-block:: python

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

Finally use the ``sloth.do_action()`` function to make PiSloth move.

.. code-block:: python

    sloth.do_action('turn left', 7, 90)
    sloth.do_action('forward', 5, 90)
    sloth.do_action('turn right', 7, 90)
    sloth.do_action('forward', 5, 90)

In general, all actions of PiSloth can be implemented with the ``sloth.do_action()`` function. It has four parameters:

* ``motion_name`` is the name of specific actions, including: ``forward``, ``turn right``, ``turn left``, ``backward``, ``stand``, ``moon walk left``, ``moon walk right``, ``hook``, ``big swing``, ``swing``, ``walk boldly``, ``walk backward boldly``, ``walk shyly``, ``walk backward shyly``, ``stomp rihgt``, ``stomp left``, ``close``, ``open``, ``tiptoe left``, ``tiptoe right``, ``fall left``, ``fall right``.
* ``step`` represents the number of each action is done, the default is 1.
* ``speed`` indicates the speed of the action, the default is 50 and the range is 0~100.
* ``bpm`` means rhythm, we will use it later in the :ref:`dance_python` project.


.. note::
    
    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla_software`.