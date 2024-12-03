class A:
    College = "Sanjivani"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(f'{self.name} , {self.rollno}, {A.College}')

    @classmethod
    def CName(cls):
        print(f'Clg : {cls.College}')    

obj = A("Ashu",111)
obj.display()            
obj.CName()        
        