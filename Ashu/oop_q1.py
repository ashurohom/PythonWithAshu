'''
Create a Class
Create a class Person with the following attributes:
Name
Age
Add a method to display the name and age of the person.
Create an object of this class and display the information.
'''

class Person:
    name = "Ashu"
    age = 24

    def display(self):
        print(f'{self.name} {self.age}')

p1 = Person()
p1.display()      