'''
Constructor with Parameters
Define a class Rectangle with attributes length and width.
Add a constructor to initialize these attributes and a method area() to calculate the area.
Create an object and calculate its area.
'''

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width
    
r1 = Rectangle(10,5)
print(r1.area())    