'''
Types of error in python
1. Syntax error
2. Runtime error

Syntax error - Comes when we dont follow proper syntactical rules 
Runtime error - Comes due to incorrect logic (also called exception)

Exception Handling
Runtime error can be handled with exception handling, but not syntax error

Syntax:
try:
    ______
    ______
except:
    ______
    ______
    
'''

# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("Entr the value of b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value")


# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("Entr the value of b:"))
#     print(a/b)
# except (ZeroDivisionError,ValueError)as message:
#     print(message)

# # default except block - generally used for writing normal message or showing normal message or showing normal error
# except:
#     print("This is defualt part of except block")


# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("Entr the value of b:"))
#     print(a/b)
# except (ZeroDivisionError,ValueError)as message:
#     print(message)
    
# else:
#     print("Everything is ok")


#finally block
# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("Entr the value of b:"))
#     print(a/b)
# except (ZeroDivisionError,ValueError)as message:
#     print(message)

# finally:
#     print("finally is always executed")


#Nested try-except block
# try:
#     a = int(input("Enter the value of a:"))
#     b = int(input("Entr the value of b:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)



#user defined exception by raise keyword
bank_bal = 500
if bank_bal < 2000:
    raise Exception("your account balance is below a accessing limit")
else:
    print("Your amount has withdrawal")