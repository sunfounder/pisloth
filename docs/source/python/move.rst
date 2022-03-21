移动
========

这是第一个项目。PiSloth 已经醒来，它可以自由移动。

.. image:: img/movement.png
  :align: center


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 move.py

运行代码后，你会看到 PiSloth 向左移动 7 步，向前移动 5 步，向右移动 7 步，向前移动 5 步。

**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from pisloth import Sloth

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

    def main():
        sloth.do_action('turn left', 7, 90)
        sloth.do_action('forward', 5, 90)
        sloth.do_action('turn right', 7, 90)
        sloth.do_action('forward', 5, 90)


    if __name__ == "__main__":
        while True:
            main()

**这个怎么运作？**

首先，在 ``pisloth`` 库中导入 ``Sloth`` 类, 它包含 PiSloth 的所有操作和实现它们的函数。

.. code-block:: python

    from pisloth import Sloth


然后实例化 ``Sloth`` 类。

.. code-block:: python

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])

最后使用 ``sloth.do_action()`` 函数使 PiSloth 移动。

.. code-block:: python

    sloth.do_action('turn left', 7, 90)
    sloth.do_action('forward', 5, 90)
    sloth.do_action('turn right', 7, 90)
    sloth.do_action('forward', 5, 90)

一般来说，PiSloth 的所有动作都可以通过 ``sloth.do_action()`` 函数来实现. 它有四个参数：

* ``motion_name`` 是具体动作的名称，包括： ``forward``, ``turn right``, ``turn left``, ``backward``, ``stand``, ``moon walk left``, ``moon walk right``, ``hook``, ``big swing``, ``swing``, ``walk boldly``, ``walk backward boldly``, ``walk shyly``, ``walk backward shyly``, ``stomp rihgt``, ``stomp left``, ``close``, ``open``, ``tiptoe left``, ``tiptoe right``, ``fall left``, ``fall right``.
* ``step`` 表示每个动作执行的次数，默认为1。
* ``speed`` 表示动作的速度，默认为50，范围为0~100。
* ``bpm`` 表示节奏，在后面 :ref:`dance_python` 示例中会用到.


.. note::
    
    您可以通过 :ref:`filezilla` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。