# Polymorphism In Class methods

class Mahindra:
    def fuel(self):
        print("Mahindra make a Diseal Engine")

    def max_speed(self):
        print("Mahindra Max Speed Is 300")

class Maruti:
    def fuel(self):
        print("Maruti Make A Only Petrol Engine")

    def max_speed(self):
        print("Maruti Max Speed Is 250")

mahi = Mahindra()
maru = Maruti()                             

# iterate objects of same type
for car in (mahi,maru):
     # call methods without checking class of object
    car.fuel()
    car.max_speed()
    print()