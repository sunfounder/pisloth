Move
========

This is the first project. PiSloth has woken up, and it moves freely.

Before programming, you need to learn the basic usage of Ezblock Studio from here.

* `Quick User Guide for Ezblock 3 <https://docs.sunfounder.com/projects/ezblock3/en/latest/quick_user_guide_for_ezblock3.html>`_

* `How to Create a New Project? <https://docs.sunfounder.com/projects/ezblock3/en/latest/create_new.html>`_

.. image:: media/movement.png
  :align: center

**TIPS**


This is the basic structure of the program, the Start block is used to do some initialization (even if no block is placed, it cannot be deleted) and the Forever block is, as the name suggests, a continuous loop that allows your program to change and respond.


.. image:: media/move8.png

This block is used to make PiSloth do a specific action several steps at a speed (%), for example, let PiSloth go forward 1 step at 50% speed.

Different actions can be selected from the drop down options, there are 22 in total.

.. image:: media/move1.png

This is a block that sets the duration of the previous block, unit: ms.

.. image:: media/move7.png




**EXAMPLE**

After writing the code according to the following figure, click the download icon in the bottom right corner, you will see PiSloth move forward 3 steps, backward 4 steps, left 3 steps, right 5 steps, and finally stop. Since the whole code is placed inside the Forever block, PiSloth will repeat the above actions after stopping for a while.

You can try putting the code from the Forever block into the Start block and see what happens.


.. image:: media/move6.png
