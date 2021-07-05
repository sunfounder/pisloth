from pisloth import Sloth
from robot_hat import Music
from robot_hat import TTS
import sys
import tty
import termios
import time

sloth = Sloth([1,2,3,4])
tts = TTS()
music = Music()
sloth.set_offset([0,0,0,0])

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

manual = '''
Press keys on keyboard to control PiSloth!

    W: Forward
    A: Turn left
    S: Backward
    D: Turn right
    1: Sound effect: talk1
    2: Sound effect: talk2
    3: Sound effect: talk3
    4: Sound effect: depress2
    Q: Say: "Oh hello there"
    E: Say: "bye"
    ESC: Quit
'''

def main():
    print(manual)
    while True:
        key = readkey()
        # print(key)
        if key == "w":
            sloth.do_action('forward', 1, 100)
        elif key == "a":
            sloth.do_action('turn left', 1, 100)
        elif key == "s":
            sloth.do_action('backward', 1, 100)
        elif key == "d":
            sloth.do_action('turn right', 1, 100)
        elif key == "1":
            music.sound_effect_play('./sounds/talk1.wav')
        elif key == "2":
            music.sound_effect_play('./sounds/talk2.wav')
        elif key == "3":
            music.sound_effect_play('./sounds/talk3.wav')
        elif key == "4":
            music.sound_effect_play('./sounds/depress2.wav')
        elif key == "q":
            tts.say("Oh hello there")
        elif key == "e":
            tts.say("bye")
        elif key == chr(27): # 27 for ESC
            break
        time.sleep(0.05)
    print("\nQuit")

if __name__ == "__main__":
    main()  