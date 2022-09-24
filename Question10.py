# Calculate multiplication of two random float numbers.

import random
def myprog():
    a=0.1
    b=1
    c=random.uniform(a,b)
    d=9.5
    e=99.5
    f=random.uniform(d,e)
    g=c*f
    print(f"The product of two randomly generated numbers {c} and {f} is {g}.")
myprog()
