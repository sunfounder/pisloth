下载代码和库
============================

首先通过在命令行中使用 ``git clone`` 下载库文件 ``robot-hat``  。

.. note:: 

    在下面的安装过程中，可能会由于网络问题导致失败，你需要参考 :ref:`pip_apt_change` 来修改配置。
    
.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://gitee.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    运行 setup.py 将下载一些必要的组件。 由于网络问题，您可能无法下载成功。您可能需要重新下载。
    在这种情况下，输入 Y 并按 Enter。
	
	.. image:: img/dowload_code.png

然后下载代码并安装 ``pisloth`` 库。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b v2.0 https://gitee.com/sunfounder/pisloth.git
    cd pisloth
    sudo python3 setup.py install


这一步需要一点时间，所以请耐心等待。

最后需要运行脚本 ``i2samp.sh`` 安装i2s功放所需的组件，否则它可能会没有声音。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/pisloth
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 y 并按 Enter 继续运行脚本。

.. image:: img/i2s2.png

输入 y 并按 Enter 让 ``/dev/zero`` 在后台运行。

.. image:: img/i2s3.png

输入 y 并按 Enter 重新启动机器。

.. note::
    
    如果重启后没有声音，你需要多次运行 ``i2samp.sh``。

