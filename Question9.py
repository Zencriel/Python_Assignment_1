#Generate and display 3 random integers between 100 and 999 which is divisible by 5.

import random
import time
def myprog():
    print("Generating 3 random numbers between 100 and 999 that are divisible by 5...")
    time.sleep(1)
    for num in range (3):
        print(random.randrange(100,999,5), end=',')

myprog()


