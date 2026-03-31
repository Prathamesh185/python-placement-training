'''
There are 3 types of method we can declare at class
1. Static
2. Instance
3. Class

Instance method - If any instance variable we are implementing inside of any method then that method will be called as instance method
Static method - We can use static method when the code that belongs to class it do not use the object
'''

# 1. Instance method
# class Hod:
#     def __init__(self, name,rollno,mob):                     
#         self.name = name                                    #instance variable
#         self.roll_no = rollno
#         self.mob = mob

#     def info(self):                                         #instance method
#         print("MY name is:",self.name)
#         print("My age is:",self.roll_no)
#         print("My emp id:",self.mob)

# obj = Hod('Arjun', 45, 101)
# obj.info()


# 2. static method
class Student:
    @staticmethod
    def get_personal_detail(firstname, lastname):
        print("your personal detail=",firstname,lastname)
    
    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("your contact detail=",mobil_no,rollno)

Student.get_personal_detail("prashant","jha")
Student.contact_detail(5456454646, 1001)