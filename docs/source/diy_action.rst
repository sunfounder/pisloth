DIY Action
===============

通过之前课程的学习，你是不是对pisloth有了更深的了解呢？那么接下来让我们尝试自己设计pisloth的动作吧。

**Code**

.. code:: python

    from pisloth import Sloth
    import time

    sloth = Sloth([1,2,3,4])
    sloth.add_action("my_action", [
        [ 45,0  ,0, 0],
        [0,   0, 0,   0]
        ])

    def main():
        sloth.do_action("my_action", 1, 80)
        time.sleep(1)
        
    if __name__ == "__main__":
        while True:
            main()  

**How it works?**

你可以通过 ``add_action`` 函数来自定义pisloth的动作，第一个参数是动作的名称，
第二个参数是个二维数组，数组里的四个参数用于控制pisloth腿部的四个舵机。我们会在
下一课进行详细介绍。

.. code:: python

    sloth = Sloth([1,2,3,4])
    sloth.add_action("my_action", [
        [ 45,0  ,0, 0],
        [0,   0, 0,   0]
        ])

然后用 ``do_action`` 函数让pisloth做动作查看实际效果。