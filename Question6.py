# Write a Python program to calculate number of days between two dates input by the user.

def myprog():
    import datetime
    a = input("Input first date (in YYYY/M/DD) ")
    b = input("Input second date (in YYYY/M/DD) ")
    c = datetime.datetime.strptime(a, "%Y/%m/%d").date()
    d = datetime.datetime.strptime(b, "%Y/%m/%d").date()
    e = c - d
    print("The number of days between these dates are ",abs(e.days))
myprog()



