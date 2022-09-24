# Guess a number from 1 - 9

import random
def myprog():
    a=random.randint(1,9)
    c=1
    while c==1:
        b=int(input("Guess number "))
        if a==b:
            print("Well Guessed")
            c=0
        else:
            print("Try again")
            c=1
myprog()