'''Access Instance Variables
Write a program to define a class Circle with:
An instance variable radius.
A method circumference() to calculate the circumference of the circle.
'''
import math

class Circle:

    def __init__(self,radius):
        self.radius=radius

    def circumference(self):
        return 2 * math.pi * self.radius    

c1 = Circle(10)
print(c1.circumference())    