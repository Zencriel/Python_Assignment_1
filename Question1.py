# Write a program to count the number of even and odd numbers from a series of numbers (1,99)

def myprog():
    a=0
    b=0
    for i in range (1,100):
        if i%2==0:
            a=a+1
        else:
            b=b+1
    print(f"there are {a} even numbers")
    print(f"there are {b} odd numbers")
myprog()
