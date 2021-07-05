
from pisloth import Sloth

sloth = Sloth([1,2,3,4])
sloth.set_offset([0,0,0,0])

def main():
    sloth.do_action('turn left', 7, 100)
    sloth.do_action('forward', 5, 100)
    sloth.do_action('turn right', 7, 100)
    sloth.do_action('forward', 5, 100)

if __name__ == "__main__":
    while True:
        main()