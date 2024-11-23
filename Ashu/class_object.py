# create a class

class College:
    dept = "Computer"
    hod = "Ashitosh"

    print(f'{dept} {hod}')
print()



# create a object of class

class School:
    name = "Om Gurudev Gurukul"
    classs = "10th"

mySchool = School()
print(mySchool.name)
print(mySchool.classs)
print()




# create instance of class

class Education:
    def __init__(self,uni,sub):
        self.uni=uni
        self.sub=sub

newEducation = Education("SPPU","Math")
print(newEducation.uni)
print(newEducation.sub)
print()




# method calling in instance variable

class Student:
    def __init__(self,name,div,rollno):
        self.name=name
        self.div=div
        self.rollno=rollno

    def Mark(self):                                     #method
        return f'{self.name}  {self.div}  {self.rollno}'


newStudent = Student("Ashu","B",111)
print(newStudent.Mark())                            #call method on the newStudent Object
print()