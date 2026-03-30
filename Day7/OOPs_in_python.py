# class Student:
#     roll_number = 101
#     num1 = 50
#     num2 = 100

#     def add(self):
#         print(self.num1 + self.num2)
#         self.name = input("Enter name:")
#         print(self.name)

# obj = Student()
# obj.add()
# print(obj.roll_number)

'''
method = function inside a class is called method
In class level or in function first argument must be self
By using constructor we initialize the object (intialize = assigning memory to object)
Constructor call automatically whenever we create a object

In python the name of constructor is __init__(self)
constructor will execute only once for 1 object 
'''

# class NewClass:
#     def __init__(self):
#         print("constructor always execute first")
#     def show(self):
#         print('welcome to class level programming')

# obj = NewClass()
# obj.show()
# obj1 = NewClass()


# Types of constructor

# 1. default constructor
# class Hod:
#     def __init__(self):                     #default constructor
#         self.name = 'prashant jha'
#         self.age = 53
#         self.emp_id = 1001

#     def info(self):
#         print("MY name is:",self.name)
#         print("My age is:",self.age)
#         print("My emp id:",self.emp_id)

# obj = Hod()
# obj.info()


# 2. parameterized constructor
class Hod:
    def __init__(self, name, age,rollno):                     #parameterized constructor
        self.name = name
        self.age = age
        self.emp_id = rollno

    def info(self):
        print("MY name is:",self.name)
        print("My age is:",self.age)
        print("My emp id:",self.emp_id)

obj = Hod('Arjun', 45, 101)
obj.info()