.. _custom_action_python:

自定义动作
==========================

在之前的项目中，我们能够给 PiSloth 自定义步态，那么我们如何将这些步态组合成动作呢？

例如，让 PiSloth 摆出上一个项目中步态，然后回到站立姿势，如此循环实现蹦蹦跳跳的效果。

.. image:: img/diy_pic.jpg
  :width: 400
  :align: center

.. note::

    您可以为您的 PiSloth 下载并打印卡通面具。
    
    * `卡通面具（.pdf） <https://gitee.com/sunfounder/sf-pdf/tree/master/%E5%8D%A1%E7%89%87/%E5%8D%A1%E9%80%9A%E9%9D%A2%E5%85%B7>`_

**第1步**: 进入 ``/home/pi/pisloth/examples`` 路径。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples

**第2步**: 打开 ``custom_action.py`` 文件。

.. raw:: html

    <run></run>

.. code-block::

    nano custom_action.py

**第3步**: 修改 ``sloth.add_action()`` 中的角度，每组代表1个步态，这里只设置了2个步态，您可以无限添加下去。

.. code-block:: python

    sloth.add_action("my_action", [
        [ 0,-45  ,0, 40],
        [0,   0, 0,   0]
        ])

**第4步**: 运行代码.

.. raw:: html

    <run></run>

.. code-block::

    sudo python3 custom_action.py



**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

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






