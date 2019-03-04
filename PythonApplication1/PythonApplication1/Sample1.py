class Sample1(object):
    """description of class"""


def factorial(n):
  
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)


    return n

    
n = eval(input("What would you like to find the factorial of: "))

print(factorial(n))