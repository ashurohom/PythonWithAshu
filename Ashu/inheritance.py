class Car:
    def __init__(self,company,name):
        self.company=company
        self.name=name

class ElectricCar(Car):
    def __init__(self, company, name, battery):
        super().__init__(company, name)
        self.battery=battery

my_ev = ElectricCar("KIA","SELTOS EV","80kwh")
print(my_ev.company)
print(my_ev.name)
print(my_ev.battery)

print()

mycar = Car("Mahindra","Bolero")
print(f'Company {mycar.company} and Car Name {mycar.name}')

