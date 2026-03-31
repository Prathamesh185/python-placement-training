'''
1. Inheritence - Code Reusability
2. Polymorphism
3. Abstraction
4. Encapsulation

1. Inheritance - process by which one object acquires the properties of another object

Base class - A class which inherits its property to another class
Inherited class - A class in which property is inherited.

Types of Inheritence
i) Single level Inheritence
ii) Multi-level Inheritence
iii) Multiple Inheritence
iv) Hierarchical 

class derived-class(base-class):
__________
__________
__________

'''

# i) single level inheritence
# class College: #parent class
#     def college_name(self):
#         print("Modern College")

# class Student(College): #child class
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")

# obj = Student()
# obj.college_name()
# obj.student_info()

'''
ii) Multi-level Inheritence
Syntax:
class GrandFather:
    _________
    _________

class Father(GrandFaterh):
    _________
    _________

class Child(Father):
    _________
    _________

'''
# class College:                                   #level-1 class
#     def college_name(self):
#         print("Modern College")

# class Student(College):                          #level-2 class
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")

# class Exam(Student):                             #level-3 class
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

'''
iii) Multiple Inheritence

Syntax :
class Parent1:
    ______
    ______
class Parent2:
    ______
    ______

class ParentN:
    ______
    ______

class Derived(Parent1,Parent2, .....)
    ______

'''
# class subjMarks:
#     math = int(input("Enter paper marks of math:"))
#     DE = int(input("Enter paper marks of design Engineering:"))
#     c = int(input("Enter paper marks of c:"))
#     English = int(input("Enter paper marks of English:"))

# class Practical:
#     cpract = int(input("Enter practical marks of C:"))

# class Result(subjMarks, Practical):
#     def total(self):
#         if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.English >= 40 and self.cpract >= 40:
#             print("Pass")
#         else:
#             print("Fail")

# obj1 = Result()
# obj1.total()

'''
Polymorphism

Poly - Many
Morph - Forms
Ability of a message to be displayed in more than one form
Eg: A person in real world an perform many task at a time like at the same time can watch TV, can eat food can receive a call

2 types of Polymorphism
i) Compile time Polymorph - Method overloading
ii) Runtime Polymorph - Method overriding
'''
# class Principal:  
#     def role(self):  
#         print("i am managing all activity of college")  
  
# class Dean:  
#     def role(self):  
#         print('Dean= I am decision taking person')  
          
# class Hod:  
#     def role(self):  
#         print('Hod= I have responsibility of Teachers and Students')         
# class Faculty:  
#     def role(self):  
#         print('Faculty= I have to complete syllabus successfully')  
        

# def  func(obj): # called func obj =1:Dean  
#     obj.role()# calling func  
# campus=[Principal(),Dean(),Hod(),Faculty()]   
# for obj in campus: #obj =[0:Principal(),1:Dean(),2:Hod()]  
#     func(obj)   # calling fun  


'''
Overloading Types
1. Method Overloading - Method name is same but arguments are different
2. Constructor Overloading 
3. 

Python doesn't support method overloading and constructor overlaoding
'''
# Method Overloading - not supported in python
# class Arithmetic:
#     def add(self, a):
#         print(a)
#     def add(self, a, b):
#         print(a+b)
#     def add(self, a, b, c):
#         print(a+b+c)

# obj = Arithmetic()
# obj.add(5)
# obj.add(5,5)
# obj.add(5,5,5)



# Method overloading - not supported
# class Arithmetic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self, a):
#         print("passing one argument")
#     def __init__(self, a, b):
#         print("Passing 2 arguments")

# obj1 = Arithmetic()
# obj2 = Arithmetic(2)
# obj3 = Arithmetic(2,3)


'''
Method Overriding - possible only if parent-child relationship exist (inheritence)
'''
# class RBI:
#     def homeLoan_ROI(self):
#         print("ROI for homeloan = 7.1%")
#     def carloan_ROI(self):
#         print("ROI for carloan = 11%")

# class SBI(RBI):
#     def homeLoan_ROI(self):
#         print("ROI for homeloan = 5.1%")

# obj1 = SBI()
# obj1.homeLoan_ROI()
# obj1.carloan_ROI()
     


# super() method - we can access parent class method in child class
# class RBI:
#     def homeLoan_ROI(self):
#         print("ROI for homeloan = 7.1%")
#     def carloan_ROI(self):
#         print("ROI for carloan = 11%")

# class SBI(RBI):
#     def homeLoan_ROI(self):
#         print("ROI for homeloan = 5.1%")
#         super().homeLoan_ROI()

# obj1 = SBI()
# obj1.homeLoan_ROI()
# obj1.carloan_ROI()


#Constructor Overriding
class Father:
    def __init__(self):
        print("I am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("I will be late for breakfast")

obj = Child()



# super consturctor - calls constructor of parent class
class Father:
    def __init__(self):
        print("I am already at breakfast table")

class Child(Father):
    def __init__(self):
        print("I will be late for breakfast")
        super().__init__()

obj = Child()
