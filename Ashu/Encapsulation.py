class Employee:
    def __init__(self,name,salary,project):
        self.__name=name
        self.__salary=salary
        self.__project=project

    def show(self):
        print(f'{self.__name} {self.__salary}')

    def work(self):
        print(f'On Project Role {self.__project}')        

emp = Employee('Ashu',50555,'Backend Developer')
emp.show()
emp.work()        


# accessing private attribute directly will cause an error
# print(emp.__name)         #attributeError
# print(emp.__salary)
# print(emp.__project)