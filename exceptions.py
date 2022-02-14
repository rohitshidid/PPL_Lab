
from unittest import case
class num2big(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

class numneg(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

try:
    num1 = input("Enter first number ")
    print(type(num1))
    num2 = input("Enter the second Number ")
    print(type(num2))
    if(num1 < 0 or num2 < 0):
        raise numneg(num1)
    i = 9
    while i>8:
        print("List of Operations")
        print("1 Add")
        print("2 Sub")
        print("3 Div")
        print("4 Mul")
        print("5 exit")
        choice = input ("Your Choice is ")
        if(choice==1):
            print("The addition is {0} ".format(num1+num2))
        elif(choice==5):
            exit(0)
        elif(choice==2):
            if(num2>num1):
                print("Num2 is grater than num1")
                raise num2big(num2)
            print("sub is {0}".format(num1-num2))
        elif(choice == 3):
            print("Division is {0}".format(num1/num2))
        elif(choice==4):
            print("Mul is {0}".format(num1*num2))
        


except NameError:
    print("Number should be an integer ")
except ZeroDivisionError:
    print("Cannot Divide by zero")
except num2big :
    print("Number 2 is grater than number 1 so it cannot be subtracted")
except numneg:
    print("Numbers cannot be negative")
