class Student:
    school_name = "Om Gurudev Gurukul  "   #class variable

    def __init__(self,name,subject):    #constructor
        self.name=name                  #instance variable
        self.subject=subject


    def stud(self):                     #new method
        return f"{self.name} {self.subject}"

print("Before : ")
s1 = Student("Ashu","python")           #create object
print(s1.name)                          #access instance variable
print(s1.subject) 
print(Student.school_name)              #access Class variable
print()       



# modify instance variable
print("After : ")
s1.name="Ashitosh"
s1.subject="Django"

# del s1.name                             #delete the instance variable

print(s1.name)
print(s1.subject)
print()

# Access Instance Variable using method
print(s1.stud())
print()

# Access Instance Variable Using getattr()

s2=Student("Rani","React")

# delattr(s2,"subject")                   #delete the instance variable

print(getattr(s2,"name"))
print(getattr(s2,"subject"))
print()


# List all Instance Variables of a Object
print(s2.__dict__)