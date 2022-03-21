遥控
==================

您还可以使用 Ezblock Studio 上的小部件使 PiSloth 移动。

.. image:: img/remote_control_pic.jpg

.. * `How to Use the Remote Control Function? <https://docs.sunfounder.com/projects/ezblock3/en/latest/remote.html>`_

**提示**

要使用远程控制功能，请从主页面左侧打开远程控制页面。

.. image:: img/control3.png

回到编程页面，您将看到一个附加的远程类别，其中出现方向键和按钮块。

* **按键 () 获取值**: 该块用于读取按钮的值，如果按钮被按下，则值为 ``1`` ，否则为 ``0`` 。
* **按键 () (按下/松开)**: 这个块与上一个块具有相同的效果，可以直接用来判断一个按钮是否被按下。
* **方向盘 () 获取 () 值**: 此块用于读取上/下/左/右（通过下拉菜单选择）键值，按下为 ``1`` ，松开为 ``0`` 。

.. image:: img/control4.png
  :width: 500


**示例**


.. note::

  你可以直接打开我们提供的示例或者是按照下图来编写程序，详细教程请参考 :ref:`open_create`。

.. image:: img/control.png

代码运行后，再次进入到 **远程控制** 页面。按下 **方向盘A** 小部件来控制PiSloth的移动，按下按键A,B,C,D来让PiSLoth发出不同的音效。
