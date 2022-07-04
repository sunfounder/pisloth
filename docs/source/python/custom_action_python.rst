.. _custom_action_python:

Custom Action
===============

In the previous project, we were able to give PiSloth custom steps, so how do we combine these steps into actions?

For example, have PiSloth make the step from the previous project and then return to the initial position.

.. image:: img/diy_pic.jpg
  :width: 400
  :align: center

.. note::

    You can download and print the `PDF Cartoon Mask <https://github.com/sunfounder/sf-pdf/tree/master/prop_card/cartoon_mask>`_ for your PiSloth.

**Step 1**: Go to the ``/home/pi/pisloth/examples`` path.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples

**Step 2**: Open ``custom_action.py`` with the following command.

.. raw:: html

    <run></run>

.. code-block::

    nano custom_action.py

**Step 3**: Modify the angle in ``sloth.add_action()``, each group represents a step, and only 2 steps are set here. You can set multiple steps as needed.

.. code-block:: python

    sloth.add_action("my_action", [
        [ 0,-45  ,0, 40],
        [0,   0, 0,   0]
        ])

**Step 4**: Run this code.

.. raw:: html

    <run></run>

.. code-block::

    sudo python3 custom_action.py



**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pisloth import Sloth
    import time

    sloth = Sloth([1,2,3,4])
    sloth.add_action("my_action", [
        [ 0,-45  ,0, 40],
        [0,   0, 0,   0]
        ])

    def main():
        sloth.do_action("my_action", 1, 80)
        time.sleep(1)
        
    if __name__ == "__main__":
        while True:
            main()  






