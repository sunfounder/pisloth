Obstacle Avoidance
=====================

In this project, when PiSloth detects an obstacle, it will send a signal and look for another direction to move forward.


**TIPS**

This is based on the previous project :ref:`Don't Touch Me`, which adds autonomous judgment, so that PiSloth can actively avoid obstacles in front of it.

**EXAMPLE**


After the code runs, PiSloth will walk forward. If it detects that the distance of the obstacle ahead is less than 10cm, it will stop and sound a warning, then turn left for 7 steps and stop. If there is no obstacle in the direction after turning left or the obstacle distance is greater than 10, it will continue to move forward.

Since the effective detection distance of the ultrasonic sensor module is 2-400cm, when the detection distance is less than it will do nothing.

.. image:: media/Obstacle.png

