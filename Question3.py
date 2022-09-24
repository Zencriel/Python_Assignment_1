# Write a Python program to create the multiplication table (from 1 to 10) of a number

def myprog():
    a=int(input("Enter a number"))
    for i in range(1,11):
        print(a, "x", i, "=", a*i)
myprog()