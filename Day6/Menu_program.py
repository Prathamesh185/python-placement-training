#WAP to do a menu driven program using arithmethic operation
import sys

def addition():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print("Addition=",a+b)

def subtraction():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print("subtraction=",a-b)

def multiplication():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print("multiplication=",a*b)

def division():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    print("Division=",a/b)


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice:"))
    if choice==1:
        addition()
    elif choice==2:
        subtraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        division()
    elif choice==5:
        sys.exit()
