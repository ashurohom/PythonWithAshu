# Public
# Private
# Protected

# Public

'''
class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):    
        print(f'{self.name}')

emp = Employee('Ashitosh')
emp.show()
'''

# Private

'''
class Employee:
    def __init__(self,name):
        self.__name=name
        print(f'{self.__name}')

    #def show(self):                 #this will run
    #     print(f'{self.__name}')

emp = Employee('Ashitosh')       
emp.__name()    #Error Private Variable Not Accessaible AttributeError:
'''


# Protected

class Employee:
    def __init__(self,name):
        self._name=name
        self._project="MyBuddy"

class Customer(Employee):
    def __init__(self, name):
        super().__init__(name)        
        print(f'Customer Name : {self._name}')

    def show(self):
        print(f'Project Name : {self._project}')

cust = Customer('Rani')        
cust.show()

