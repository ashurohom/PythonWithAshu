# # class

# # class Student:
# #     name="Ashitosh"

# # s1=Student()
# # s2=Student()
# # print(s1.name)    
# # print(s2.name)    


# # Example

# class College:
#     student = "Ashitosh"
#     teacher = "S A Patil "
#     subject = "Python"

# c=College()
# print(c.student)
# print(c.teacher)
# print(c.subject)

# print(f'{c.student} is a student and {c.teacher} teach a {c.subject}')

# # Example 2

# class Car:
#     Company = "Mahindra"
#     Name = 'Bolero'

# c1=Car()
# print(c1.Company)
# print(c1.Name)    


# # ------------------------------------------------------------------------------------------------------------------

# # __init__ = call constructor

# # EXAMPLE 1

# class Car :
#     def __init__(self,brand,model):     #Define Constructor
#         self.brand=brand
#         self.model=model

# new_car = Car("KIA","Seltos")           # call object
# print(f'Car Brand {new_car.brand}')        
# print(f'Car Model {new_car.model}')        



# print()
# # EXAMPLE 2

# class Character:
#     def __init__(self,name,power):
#         self.name=name
#         self.power=power
# hero = Character("Shaktiman",100)
# print(f'Hero Name {hero.name}')        
# print(f'hero power {hero.power}')        


class State:
    def __init__(self,dist,taluka):
        self.dist=dist
        self.taluka=taluka

    def new_state(self):
        return f'{self.dist} {self.taluka}'


mystate = State("Ahilyanagar","Kopargaon")
print(f'{mystate.dist}')        #Ahilyanagar
print(f'{mystate.taluka}')      #Kopargaon  

print(mystate.new_state())      #Ahilyanagar Kopargaon


# Practice

class Car:
    def __init__(self,company,name):
        self.company=company
        self.name=name

    def Selfcar(self):
        return f'{self.company}{self.name}'

mycar = Car("Mahindra","Bolero")
mycar2 = Car("Maruti","Alto")
mycar3 = Car("KIA","Seltos")

print(f'Company {mycar.company} and Car Name {mycar.name}')
print(f'Company {mycar2.company} and Car Name {mycar2.name}')
print(f'Company {mycar3.company} and Car Name {mycar3.name}')

print(mycar.Selfcar())
