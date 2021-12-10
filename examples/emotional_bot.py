
from pisloth import Sloth
from robot_hat import TTS, Music
import time

tts = TTS()
music = Music()

sloth = Sloth([1,2,3,4])
sloth.set_offset([0,0,0,0])

def confuse():
    try:
        music.sound_effect_threading('./sounds/sign.wav')
    except Exception as e:
        print(e)
    sloth.do_action('hook', 1, 100)  

def happy():
    try:
        music.sound_effect_threading('./sounds/happy2.wav')
    except Exception as e:
        print(e)
    for i in range(3):
        sloth.do_action('hook', 1, 100)
        sloth.do_action('stand', 1, 100)

def fear():
    try:
        music.sound_effect_threading('./sounds/warning.wav')
    except Exception as e:
        print(e)
    sloth.do_action('hook', 1, 100)
    sloth.do_action('stand', 1, 100)
    try:
        music.sound_effect_threading('./sounds/warning.wav')
    except Exception as e:
        print(e)
    sloth.do_action('walk backward boldly', 1, 100)
    sloth.do_action('stand', 1, 100)

def sad():
    try:
        music.sound_effect_threading('./sounds/depress.wav')
    except Exception as e:
        print(e)
    sloth.do_action('big swing', 1, 100)  

def angry():
    try:
        music.sound_effect_threading('./sounds/error.wav')
    except Exception as e:
        print(e)
    sloth.do_action('walk backward boldly', 1, 100)  
    sloth.do_action('stand', 1, 100)

def fail():
    try:
        music.sound_effect_threading('./sounds/depress2.wav')
    except Exception as e:
        print(e)
    sloth.do_action('fall left', 1, 100)  

def shy():
    try:
        music.sound_effect_threading('./sounds/talk3.wav')
    except Exception as e:
        print(e)
    sloth.do_action('close', 1, 100)  
    time.sleep(1)    
    try:
        music.sound_effect_threading('./sounds/talk2.wav')
    except Exception as e:
        print(e)
    sloth.do_action('stand', 1, 100)    

def main():

    print("shy")
    shy()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("confuse")
    confuse()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("happy")
    happy()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("fear")
    fear()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("sad")
    sad()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("angry")
    angry()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)

    print("fail")
    fail()
    time.sleep(1)
    sloth.do_action('stand', 1, 100)
    time.sleep(2)       


if __name__ == "__main__":
    while True:
        main()