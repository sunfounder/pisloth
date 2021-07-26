from robot_hat import TTS, Music
import time
import os

tts = TTS()
music = Music()

def main():
    # # tts.say('Oh, hello there')
    # # tts.say("Here are all the sound effects i can do")
    for file in os.listdir("./sounds"):
        name = file.split(".")[0]
        print(name)
        # tts.say(name)
        time.sleep(1)
        try:
            music.sound_effect_play('./sounds/%s' % file)
        except Exception as e:
            print(e)
        time.sleep(2)
    # music.sound_effect_play('./sounds/happy2.wav')
    # music.sound_effect_play('./sounds/happy.wav')

if __name__ == "__main__":
    main()  