import math
a = 0
b = 1
x = eval(input("Which number in the sequence do you wish to find: "))

def fSequence():
    global x
    c = 0
    d = 1
    for i in range(0 , math.ceil(x/2 - 1)):
        c = c + d
        d = c + d

    if (x == 1):
        print("0")
    if (x == 2):
        print("1")

    if (x >= 3):
        if (x % 2 > 0):
            print(c)
        if (x % 2 == 0):
            print(d)
    

fSequence()