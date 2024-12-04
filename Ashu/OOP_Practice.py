class A:
    bike = "Dream Bike : FZ-S"

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'Constructor : {self.bike}')

    def display(self):    
        print(f'{self.name},{self.age},{self.bike}')
        print(f'Using Class Name : {A.bike}')

    @classmethod
    def show(cls):
        print(f'Class Method : {cls.bike}')

obj = A("Ashu",24)
obj.name="Rani"
# del obj.name
obj.age=22
obj.display()
obj.show()
print(f'Class Variable : {A.bike}')
