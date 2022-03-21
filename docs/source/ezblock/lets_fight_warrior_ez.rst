战斗吧！勇士！
=======================

在这里，PiSloth 是一个勇敢的战士，当它出现在敌人面前时，它会发出咆哮冲向敌人。

.. image:: img/warrir.jpg
  :width: 400
  :align: center

.. note::

    您可以为您的 PiSloth 下载并打印卡通面具。
    
    * `卡通面具（.pdf） <https://gitee.com/sunfounder/sf-pdf/tree/master/%E5%8D%A1%E7%89%87/%E5%8D%A1%E9%80%9A%E9%9D%A2%E5%85%B7>`_

**提示**

您可能希望使用 **变量** 来简化您的程序。例如，当你有多个函数需要读取障碍物距离时，你不需要读取每个函数的值，只需将值加载到一个 **变量** 中并多次使用即可。

.. image:: img/sp210512_114830.png

单击 **变量** 类别上的 **创建变量** 按钮以创建名为距离的变量。

.. image:: img/sp210512_114916.png
  :width: 800

您可以使用此块来设置无限循环。

.. image:: img/fight1.png


这是一个跳出循环的块，它有两个选项，只能在循环内使用。


* 中断循环：跳出整个循环。
* 继续下一次循环：跳出当次循环，进入下一次。

.. image:: img/fight2.png


**示例**

.. note::

  你可以直接打开我们提供的示例或者是按照下图来编写程序，详细教程请参考 :ref:`open_create`。

.. image:: img/fight.png

代码运行后，PiSloth会不断检测障碍物的距离，当距离在5到40之间时，PiSloth会发出轰鸣声并向前冲去；当障碍物的距离小于 5 时，PiSloth 将停止。

**流程图**

.. image:: img/flowchart_fight.png
