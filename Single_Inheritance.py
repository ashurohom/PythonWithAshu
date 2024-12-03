#single Inheritance

class Car:
    def Company(self):
        print(f"Car Company : Mahindra")

    def Model(self):
        print(f"Car Model : Bolero")

class Tractor(Car):
    def Companys(self):
        print(f'Tractor Company : John Deere')

    def Models(self):
        print(f"Tractor Model : 5050D")                

obj = Tractor()
obj.Company()
obj.Model()
obj.Companys()
obj.Models()

