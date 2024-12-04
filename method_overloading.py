#Method Overloading

class A:
    def name(self,name):
        self.name=name
        print(f"Hello")


class B(A):
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(f'{self.name},{self.rollno}')    
        print(f'Welcome')

obj = B("Ashu",111)
obj.display()   
     
