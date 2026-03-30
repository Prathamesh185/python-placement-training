# Types of variables in class
'''
1. Instance variable
2. Static variable
3. Local variable
'''
# 1. Instance variable - creates seperate memory for each object
# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# obj1.a = 20

# print(obj1.a) #only obj1.a value changes, because seperate memory
# print(obj2.a)
# print(obj3.a)

# 2. Static Variable - creates common memory for all objects
'''
1 static variable = 1 memory
How to access static variable? There are 2 ways to access static variable the first one is by class name or second way by object but programmer
recommended to access by class name

By using object or self variable we can access or read static variable but we can not do modification or deletion
If we try to delete it, it gives error 
'''

class New:
    a = 10
    def __init__(self):
        self.name = "prashant"

obj1 = New()
obj2 = New()
obj3 = New()
print(obj1.a)
print(obj2.a)
print(obj3.a)

New.a = 50
print(obj1.a)
print(obj2.a)
print(obj3.a)