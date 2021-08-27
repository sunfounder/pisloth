
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
    sloth.do_action('stomp right',3,bpm=129)
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
