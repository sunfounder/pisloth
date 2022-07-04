Remote Control
==================

You can also use the widgets on EzBlock Studio to make PiSloth move.

.. image:: img/remote_control_pic.jpg

* :ref:`ezblock:remote_control_latest`


**TIPS**

To use the remote control function, you need to enter the **Remote Control** page from the left side of main page, and then drag one D-pad and 4 buttons to the central area.

.. image:: img/control3.png

Back in the programming page, you will see an additional Remote category, and the D-pad and Button block appear in it.

* **Button () get value**: This block is used to read the value of the buttons, if the button is pressed, the value is 1, otherwise it is 0.
* **Button () is (press/release)**: This block and ``Button () get value = (0/1)`` have the same effect and can be used directly to determine whether a button is pressed or not.
* **D-pad () get () value**: This block is used to read the up/down/left/right (selected through the drop-down menu) pad values, press for 1 and release for 0.

.. image:: img/control4.png
  :width: 500


**EXAMPLE**

.. note::
    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`

    * Or find the code with the same name on the Examples page of the EzBlock Studio and click Run or Edit directly.


.. image:: img/control.png