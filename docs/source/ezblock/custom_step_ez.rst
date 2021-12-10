自定义步态
===============

在之前的项目中，我们使用了很多我们自己写的动作，那么这些动作是如何组合和完成的呢？一般来说，一个动作由一个或多个步态组成。

在这个项目中，我们将学习如何自定义 PiSloth 的步态。

我们要做的就是使用遥控器页面中的按钮，让PiSloth完成下图所示的步态，然后得到4个舵机此时的角度。

.. image:: media/diy_pic.jpg
  :width: 400
  :align: center

.. note::

    您可以为您的 PiSloth 下载并打印卡通面具。
    
    .. `PDF Cartoon Mask <https://github.com/sunfounder/sf-pdf/tree/master/prop_card/cartoon_mask>`_ for your PiSloth.

**第1步：** 在遥控器中拖出9个按钮来控制PiSloth上4个舵机的旋转角度。

.. image:: media/DIYII1.png

**第2步：** 创建 4 个变量来存储 4 个舵机的角度。

.. image:: media/DIYII2.png
  :width: 600

然后将角度初始化为 0。

.. image:: media/DIYII3.png


**第3步：** 读取用于控制舵机角度的不同按钮的值。

* **按钮AB** 控制 **左腿**。
* **按钮CD** 控制 **左脚**。
* **按钮EF** 控制 **右腿**。
* **按钮GH** 控制 **右脚**。
* 按 **按钮I**，在调试监视器中打印 4 个舵机的角度。

.. image:: media/DIYII4.png

**第4步：** 在 **循环** 块的末尾，填写读取到 4 个舵机中的角度值，并使用 **执行动作** 块让 PiSloth 执行此步骤。

.. image:: media/DIYII7.png

**第5步：** 代码完成后，点击右下角的 **下载** 图标下载并运行代码。 现在我们可以点击 **按钮 CD** 和 **按钮 GH** （根据实际代码）使PiSloth姿势像这样，你也可以让它做其他步骤。

.. image:: media/diy_pic.jpg
  :width: 400
  :align: center

**第6步:** 点击左下角的小虫子图标打开调试监视器，当你按下 **按钮I** 时，你会在调试监视器中看到4个舵机的角度。

.. note::

  如果出现多组数据，是因为点击按钮的时间长了一点，Ezblock会认为按钮被点击了数次。如果数据看着很杂乱，可以点调试监视器的右上角的清除按钮。

.. image:: media/DIYII5.png

完整代码如下：

.. image:: media/DIYII.png