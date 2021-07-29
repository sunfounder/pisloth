
from pisloth import Sloth
import time

sloth = Sloth([1,2,3,4])
sloth.add_action("my_action", [
    [ 45,0  ,0, 0],
    [0,   0, 0,   0]
    ])

def main():
    sloth.do_action("my_action", 1, 80)
    time.sleep(1)
	
if __name__ == "__main__":
    while True:
        main()  