from pynput.keyboard import Key,Controller
import time 
import random





#pip install pynput

kbd = Controller()

input('press Enter to start')

def pause(t):

    while (t>0):
        print(f'Time Left:{t}')
        t-=1
        time.sleep(1)



while True:
    nouns = ("puppy" , "rabbit" , "girl" , "monkey", "Kkgameryt", "MCguitardude", "Rebbo2818")
    verbs = ("runs" , "hits" , "jumps", "drives", "barfs", "MLG", "Swim") 
    adv = ("crazily " , "dutifully" , "foolishly", "merrily", "occasionally", "in Lava", "was shot")
    adj = ("adorable" , "clueless" , "dirty", "stupid", "and died", "lmfaooo", "By Rebbo2818")

    num = (random.randint(0,6))
    num1 = (random.randint(0,6))
    num2 = (random.randint(0,6))
    num3 = (random.randint(0,6))
    kbd.type(nouns[num] + ' ' + verbs[num1] + ' ' + adv[num2] + ' ' + adj[num3])
	#this is the text that is typed out, leave the quotation marks

    kbd.press(Key.enter)
    kbd.release(Key.enter)
    print('Command Sent')
    pause(random.randint(30,40))


