class A:
    c=10    #class variable
    def __init__(self,name,age):
        self.name=name  #instance variable
        self.age=age
        print(f'{self.name}{self.age}')

    def show(self): #instance method
        print(f'{self.name}{self.age}{self.c}')

    @classmethod
    def display(cls):
        print("Dsiplay",cls.c)
           
a=A("Ashu",24)       
a.show() 
print(a.name)
print(a.age)
print(A.c)
a.display()