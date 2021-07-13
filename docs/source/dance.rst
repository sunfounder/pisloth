Dance
=========

在这个项目中，我们会播放一段音乐，并让Pisloth跟着音乐的节奏来跳一段舞。

You can open ``dancing.py`` in the folder of the ``example`` or directly copy the following code to the Python IDE to run.

**Code**

.. code:: python

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
        sloth.do_action('stomp rihgt',3,bpm=129)
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

**How it works?**

你可以通过导入下面的这个库来让pisloth播放音乐。

.. code:: python

    from robot_hat import TTS, Music

播放musics目录下的背景音乐并设置音量为20。

.. code:: python

    music.background_music('./musics/india-Arulo.mp3')
    music.music_set_volume(20)

执行函数 ``sloth.do_action(motion_name,step=1,speed=None,bpm=None)`` 让pisloth执行设定好的动作。
这里的bpm参数会影响pisloth做动作的间隔时间，数值越大，间隔时间越短。
当我们通过一些方法了解到一首音乐的bpm后，你可以根据这首音乐的bpm自由搭配pisloth的动作，来让它伴随不同风格的音乐跳
不同风格的舞蹈。

对于音乐的bmp，如果你想了解更多，可以参考:
https://en.wikipedia.org/wiki/Tempo