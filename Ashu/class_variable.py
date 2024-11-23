# Access Class Variable in the constructor
# Access Class Variable in Instance method and outside class

class Student:
    clg_name = "Sanjiavni COE"

    def __init__(self,name):
        self.name=name    
           # access class variable inside constructor using self
        print(self.clg_name)

            #access using class name
        print(Student.clg_name)


    def new_student(self):

            # in method access using self
        print(self.clg_name)

            # in method access using class name
        print(Student.clg_name)   

s1=Student("Ashu")
s1.new_student()

print()
print(f'Outside Class using object refrence : {s1.clg_name}')
print(f'Outside Class using class name : {Student.clg_name}')
print()

# Modify Class Variables

Student.clg_name="Sanjivani College"
print(f'After')
s1.new_student()