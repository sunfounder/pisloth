
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

alert_distance = 10

def main():
    distance = sonar.read()
    if distance < 0:
        pass
    elif distance <= alert_distance:
        try:
            music.sound_effect_threading('./sounds/sign.wav')
        except Exception as e:
            print(e)
        sloth.do_action('hook', 1,95)
        sloth.do_action('stand', 1,95)
        time.sleep(0.2)
        sloth.do_action('turn left',7,95)
        sloth.do_action('stand', 1,95)
        time.sleep(0.2)
    else :
        sloth.do_action('forward', 1,95)


if __name__ == "__main__":
    while True:
        main()