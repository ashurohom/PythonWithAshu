'''
Question 1: Employee Management System
Create a class named Employee with the following requirements:

Attributes:
name: A string representing the employee's name.
id: An integer representing the employee's unique ID.
salary: A float representing the employee's salary.
Methods:
display_details(): Prints the employee's details in a readable format.
update_salary(new_salary): Updates the employee's salary to new_salary.
Task:
Create three employee objects with different details.
Update the salary of one employee.
Display the details of all employees.
'''

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def Display_Details(self):
        print(f'Name : {self.name}, ID : {self.id}, Salary : {self.salary}')

    def update_salary(self,new_salary):
        self.salary=new_salary
        print(f'Salary Updated : {self.salary}')

Emp = Employee("Ashu",1234,52411)
Emp.Display_Details()
print()
Emp.update_salary(60000)        
Emp.Display_Details()