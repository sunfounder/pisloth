
.. _dance_python:

跳舞
=========

当当当当，有请 PiSltoh 向大家展示他新学的舞蹈。

.. image:: img/dance_pic.jpg
    :width: 400
    :align: center


.. note::

    您可以为您的 PiSloth 下载并打印卡通面具。
    
    * `卡通面具（.pdf） <https://gitee.com/sunfounder/sf-pdf/tree/master/%E5%8D%A1%E7%89%87/%E5%8D%A1%E9%80%9A%E9%9D%A2%E5%85%B7>`_

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth/examples
    sudo python3 dancing.py


整个舞蹈分为2个部分，PiSloth会随着音乐完成这2个部分。如果你不暂停代码，它会重复跳舞一直跳下去。


**代码**

.. .. note::
..     You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``pisloth\examples``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python


    from pisloth import Sloth
    from robot_hat import Music
    from robot_hat import Ultrasonic
    from robot_hat import Pin
    import time
    import os

    music = Music()

    sloth = Sloth([1,2,3,4])
    sloth.set_offset([0,0,0,0])


    def main():
    
        music.background_music('./musics/india-Arulo.mp3')
        music.music_set_volume(20)
        sloth.do_action('stomp left',3,bpm=129)
        sloth.do_action('stomp right',3,bpm=129)
        sloth.do_action('moon walk left',3,bpm=129)
        sloth.do_action('moon walk right',3,bpm=129)
        for i in range(3):
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        for i in range(3):
            sloth.do_action('close',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
            sloth.do_action('open',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        sloth.do_action('tiptoe left',2,bpm=129)
        sloth.do_action('tiptoe right',2,bpm=129)

        sloth.do_action('stomp left',3,bpm=129)
        sloth.do_action('stomp rihgt',3,bpm=129)
        sloth.do_action('moon walk left',3,bpm=129)
        sloth.do_action('moon walk right',3,bpm=129)
        for i in range(3):
            sloth.do_action('hook',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)
        for i in range(4):
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('big swing',1,bpm=129)
            sloth.do_action('swing',1,bpm=129)
            sloth.do_action('stand',1,bpm=129)

        sloth.do_action('tiptoe right',2,bpm=129)
        sloth.do_action('stand',2,bpm=129)



        music.music_stop()
        time.sleep(10)



    if __name__ == "__main__":
        while True:
            main()


**这个怎么运作？**

您可以通过导入以下库让 PiSloth 播放音乐。

.. code-block:: python

    from robot_hat import TTS, Music

播放 ``pisloth/examples/musics`` 目录中的背景音乐，音量设置为20。您也可以通过 :ref:`filezilla` 将音乐添加到 ``musics`` 文件夹中。

.. code-block:: python

    music.background_music('./musics/india-Arulo.mp3')
    music.music_set_volume(20)

一般情况下，PiSloth 的所有动作都可以通过该 ``sloth.do_action()`` 函数实现。它有四个参数：


* ``motion_name`` 是具体动作的名称，包括： ``forward``, ``turn right``, ``turn left``, ``backward``, ``stand``, ``moon walk left``, ``moon walk right``, ``hook``, ``big swing``, ``swing``, ``walk boldly``, ``walk backward boldly``, ``walk shyly``, ``walk backward shyly``, ``stomp rihgt``, ``stomp left``, ``close``, ``open``, ``tiptoe left``, ``tiptoe right``, ``fall left``, ``fall right``.
* ``step`` 表示每个动作执行的次数，默认为1。
* ``speed`` 表示动作的速度，默认为50，范围为0~100。
* ``bpm`` 表示节奏，这里的bpm参数影响PiSloth运动的间隔时间。值越高，间隔时间越短。当我们通过bpm计算器知道一首歌的节拍时，我们可以让 PiSloth 随着音乐跳舞。



.. note::
    
    您可以通过 :ref:`filezilla` 向 ``musics`` 或 ``sounds`` 文件夹添加不同的音效或音乐。