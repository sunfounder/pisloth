Custom Action
=============================

In the previous project, we were able to give PiSloth custom steps, so how do we combine these steps into actions?

For example, have PiSloth make the step from the previous project and then return to the initial position.

.. image:: img/diy_pic.jpg
  :width: 400
  :align: center

.. note::

  You can download and print the `PDF Cartoon Mask <https://github.com/sunfounder/sf-pdf/tree/master/prop_card/cartoon_mask>`_ for your PiSloth.


**TIPS**

Create a variable **up_down** to store this action.

.. image:: img/up_down.png

You can use the **create action** block to make PiSloth do this action. These values ​​represent the angles of the 4 Servos on the PiSloth. The range is (-90~90).

.. image:: img/DIY2.png

Here you can increase or decrease the number of items by dragging it.

.. image:: img/DIY3.png

Fill in the angle obtained in the previous project and name this action **up_down** (drag it from **Variables** category).

.. image:: img/diy_up.png

Use the **do** block to make PiSloth do this action once at 50% speed.

.. image:: img/DIY6.png

**EXAMPLE**

.. note::
    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`

    * Or find the code with the same name on the Examples page of the EzBlock Studio and click Run or Edit directly.

.. image:: img/DIY7.png