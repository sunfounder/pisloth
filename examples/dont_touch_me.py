
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
sonar = Ultrasonic(Pin("D0") ,Pin("D1"))

alert_distance = 20

def main():
    distance = sonar.read()
    print(distance)
    if distance <= alert_distance :
        try:
            music.sound_effect_threading('./sounds/talk3.wav')
        except Exception as e:
            print(e)
        sloth.do_action('backward', 2, 100)
    else:
        sloth.do_action('stop', 1, 100)
        time.sleep(1)


if __name__ == "__main__":
    while True:
        main()