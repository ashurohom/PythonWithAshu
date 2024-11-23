class Exam:
    def __init__(self,subject,marks):
        self.subject=subject
        self.marks=marks

    def myExam(self):
        return f'Subject : {self.subject}, Marks : {self.marks}'    

e1=Exam("Python",80)    
print(e1.myExam())             #call instance method
print()

e2=Exam("React",85)
print(f'{e2.myExam()}')

