
from pisloth import Sloth
from robot_hat import TTS, Music
from robot_hat import Ultrasonic
from robot_hat import Pin
import time
import os

tts = TTS()
music = Music()

sloth = Sloth([1,2,3,4])
sloth.set_offset([0,0,0,0])
# sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

def step_on_rhythm(action_name,duration,speed):
    clk=time.time()
    count=0
    print(action_name)
    while True:
        count=count+1
        sloth.do_action(action_name,1,speed)
        time_cost=time.time()-clk
        if time_cost >= duration:
            print(count," times &",time_cost, "s")
            break


def main():
    # list = {'forward','turn left','turn right','backward','stop','hate','alarm','boring','excited','laugh','shy'}
    
    # music.background_music('./musics/india-Arulo.mp3')
    # music.music_set_volume(10)
    
    try:
        music.sound_effect_play('./sounds/sign.wav')
    except Exception as e:
        print(e)
    sloth.do_action('swing', 1, 100)
    
    time.sleep(1)



if __name__ == "__main__":
    while True:
        main()