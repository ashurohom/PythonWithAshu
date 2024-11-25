class Vehical:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def show(self):
        print(f'Details : {self.name} {self.speed}')

    def Vname(self):
        print(f'Vehical Name : Eicher')

    def Vspeed(self):
        print(f'Vehical Speed : 200')

class Car(Vehical):
    def Vname(self):
        print(f'Car Name : Bolero')

    def Vspeed(self):
        print(f'Car Speed : 350')

car=Car('Bolero',350)
car.show()

car.Vname()
car.Vspeed()

print()

vehical = Vehical('Eicher',150)
vehical.show()

vehical.Vname()
vehical.Vspeed()