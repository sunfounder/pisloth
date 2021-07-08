
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

# def main():
#     # tts.say('Oh, hello there')
#     # tts.say("Here are all the sound effects i can do")
#     for file in os.listdir("./sounds"):
#         name = file.split(".")[0]
#         print(name)
#         # tts.say(name)
#         time.sleep(1)
#         try:
#             music.sound_effect_play('./sounds/%s' % file)
#         except Exception as e:
#             print(e)
#         time.sleep(2)
#     # music.sound_effect_play('./sounds/talk1.wav')

alert_distance = 40
contact_distance = 5

def main():
    distance = sonar.read()
    print(distance)
    if distance <= alert_distance :
        while True:
            if(sonar.read()<=contact_distance):
                break
            try:
                music.sound_effect_threading('./sounds/warning.wav')
            except Exception as e:
                print(e)
            sloth.do_action('forward', 1, 100)
    sloth.do_action('stop', 1, 100)
    time.sleep(1)


if __name__ == "__main__":
    while True:
        main()