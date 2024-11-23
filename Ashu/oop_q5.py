'''
Intermediate Level

Student Details
Define a class Student with the following:
Constructor to initialize name, roll_number, and marks.
Method display_details() to show all details.
Method update_marks() to update the marks of the student.
'''
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def DisplayDetails(self):
        print(f'{self.name}')   
        print(f'{self.rollno}')   
        print(f'{self.marks}')   

    def UpdateMarks(self):
        self.marks=90

s1=Student("Ashu",111,85)
s1.DisplayDetails() 
s1.UpdateMarks()
s1.DisplayDetails()      