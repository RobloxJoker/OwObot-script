from pynput.keyboard import Key,Controller
import time 
import random

kbd = Controller()

input('press Enter to start')

def pause(t):
    while (t>0):
        print(f'Time Left:{t}')
        t-=1
        time.sleep(1)

while True:
    kbd.type('oh')
    kbd.press(Key.enter)
    kbd.release(Key.enter)
    print('Command Sent')
    pause(random.randint(17,24))
