class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):    
        print(f'{self.name},{self.age}')

obj = A("Ashu",24)
obj.name="Rani"
# del obj.name
obj.age=22
obj.display()
