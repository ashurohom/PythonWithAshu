class Public:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(f'Public Inside Class : {self.name},{self.rollno}')    

obj1 = Public("Ashu",111)
obj1.display()        
print(f'Public Outside Class : {obj1.name},{obj1.rollno}')    


print()

class Private:
    def __init__(self,name,rollno):
        self.__name=name
        self.__rollno=rollno

    def display(self):
        print(f'Private Inside Class : {self.__name},{self.__rollno}')    

obj2 = Private("Ashu",111)
obj2.display()        
print(f'Private Outside Class (via name mangling): {obj2._Private__name}, {obj2._Private__rollno}')

# print(f'Private Outside Class : {obj1.__name},{obj1.__rollno}')    Not Accessable


print()


class Protected:
    def __init__(self, name, rollno):
        self._name = name
        self._rollno = rollno
        print(f'Protected Inside Class: {self._name}, {self._rollno}')    

class Protected2(Protected):
    def __init__(self, name, rollno):
        super().__init__(name, rollno)

    def shows(self):    
        print(f'Protected In Sub Class: {self._name}, {self._rollno}')

# Create an instance of Protected2 (not Protected) to call shows
obj3 = Protected2("Ashu", 111)
obj3.shows()  

# Accessing attributes outside the class using the instance
print(f'Protected Outside Class (via object): {obj3._name}, {obj3._rollno}')

