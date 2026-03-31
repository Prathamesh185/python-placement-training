'''
Hide the complexity and show only essential part

Rule for Abstract Based Class - 
Atleast one abstract method must be there

Abstract method - have declaration but not implementation
'''

from abc import ABC, abstractmethod
class Help4Code:
    @abstractmethod
    def training(self):
        pass

    def placement(self):
        pass

class Manoj(Help4Code):
    def training(self):
        print('C, Java, C++')
    
    def placement(self):
        print('Java placement')

class Prashant(Help4Code):
    def training(self):
        print('Python, Machine Learning')
    
    def placement(self):
        print('Machine Learning placement students')

class Ankush(Help4Code):
    def training(self):
        print('HTML, CSS, JS')
    
    def placement(self):
        print('Web Development placement students')

class Ashish(Help4Code):
    def training(self):
        print('MySQL, MongoDB')
    
    def placement(self):
        print('Database Management placement students')

obj1 = Manoj()
obj1.training()
obj1.placement()

obj2 = Prashant()
obj2.training()
obj2.placement()

obj3 = Ankush()
obj3.training()
obj3.placement()

obj4 = Ashish()
obj4.training()
obj4.placement()



