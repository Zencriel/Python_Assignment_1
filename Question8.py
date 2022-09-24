# Accept number from user and calculate the sum of all numbers between 1 and given number. For example: user given 10 so the output should be 55

import math
def myprog():
    a=int(input("Enter your number "))
    b=sum(range(1,a+1))
    print(f"The sum is {b}.")
myprog()
