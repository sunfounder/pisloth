.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Download and Run the Code
============================

We can download the files by using ``git clone`` in the command line.

Install ``robot-hat`` library first.



.. code-block::

    cd ~/git clone https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 install.py

.. note::
    Running setup.py will download some necessary components. You may fail to download due to network problems. You may need to download again at this time.
    In the following cases, enter Y and press Enter.
	
	.. image:: img/dowload_code.png

Then download the code and install ``pisloth`` library.



.. code-block::

    cd ~/git clone -b v2.0 https://github.com/sunfounder/pisloth.git
    cd pisloth
    sudo python3 setup.py install


This step will take a little time, so please be patient.

Finally, you need to run the script ``i2samp.sh`` to install the components required by the i2s amplifier, otherwise the pislot will have no sound.



.. code-block::

    cd ~/robot-hat
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Type y and press Enter to continue running the script.

.. image:: img/i2s2.png

Type y and press Enter to run ``/dev/zero`` in the background.

.. image:: img/i2s3.png

Type y and press Enter to restart the machine.

.. note::
    If there is no sound after restarting, you may need to run the i2samp.sh script multiple times.