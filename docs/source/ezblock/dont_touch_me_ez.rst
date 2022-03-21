别碰我
==================

如果它看到你伸手想去摸它，它会生气并离你远远的。

**提示**

您可以直接使用此块读取与前方障碍物的距离。

.. note::

    如在组装时，Trig和Echo分别接在D2和D3上，编程时也需要同时更改。

.. image:: img/Obstacle1.png

要实现条件判断，需要使用 **如果-执行** 块。

当需要实现多个条件判断时，就得把if do改成if else do。这可以通过单击设置图标来实现。

.. image:: img/Obstacle2.png

您需要将条件语句块与 **如果-执行** 结合使用。判断条件可以是“=”、“>”、“<”、“≥”、“≤”、“≠”。

.. image:: img/Obstacle3.png

一个数字块。

.. image:: img/Obstacle4.png

该块可以发出一些预设的音效，如警笛声、枪声等。音量范围为1~100。

.. image:: img/Obstacle5.png


**示例**

.. note::

  你可以直接打开我们提供的示例或者是按照下图来编写程序，详细教程请参考 :ref:`open_create`。

.. image:: img/no_touch.png

代码运行后，当你的手靠近PiSloth, 它会发出警告声并后退。