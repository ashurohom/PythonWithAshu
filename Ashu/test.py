# inheritance

class Laptop:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Parts(Laptop):
    def __init__(self,name,price,ssd):
        super().__init__(name,price)
        self.ssd=ssd

NewParts = Parts("ASUS",78000,"1TB")
print(f'Name {NewParts.name}')
print(f'Price {NewParts.price}')
print(f'SSD {NewParts.ssd}')


# MyLaptop = Laptop("ASUS",78000)
# print(MyLaptop.name)
# print(MyLaptop.price)

x=10
y=20
print(x>y or x==10)