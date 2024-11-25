class Teacher:
    def TeacherInfo(self,name,id):
        self.name=name
        self.id=id
        print(f'{self.name} id is {self.id}\n')

class Student:
    def StudetInfo(self,sname,srollno):
        self.sname=sname
        self.srollno=srollno
        print(f'Student Name {self.sname} And RollNo Is {self.srollno}\n')    

class College(Teacher,Student):
    def CollegeInfo(self,cname,crno):
        self.cname=cname
        self.crno=crno
        print(f'Clg Name {self.cname} and Reg No Is {self.crno}\n')

clg = College()
clg.CollegeInfo('Sanjivani',12315)
clg.TeacherInfo('Sangale Sir',123)
clg.StudetInfo('Ashitosh',111)



