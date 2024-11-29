
#decoretor nd class variable

class B:
    course = "Python"   #class variable
    def __init__(self,name):
        self.name=name
        print(f'Name : {self.name}')

    @classmethod
    def display(cls):
        print("Course : ",{cls.course})

b=B("Ashu")            
b.display()