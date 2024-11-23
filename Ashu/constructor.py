# constructor

class Student:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

    def new_student(self,rollno):
        self.rollno=rollno
        print(f'{self.name} {self.subject} {self.rollno}')

s1=Student("Ashu","Python")
s1.new_student(111)




# Default Constructor

class Employee:

    def display(self):
        print('Inside Display')

emp = Employee()
emp.display()





# Non-Parameterized Constructor

class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()




# Parameterized Constructor

class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)

# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()



# Constructor With Default Values

class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)

# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()
