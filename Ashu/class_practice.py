# create a class and object example

class laptop:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def new_laptop(self):
        return(f'{self.name} {self.price}')

my_laptop = laptop("Lenovo",85000)
print(f'Laptop Name {my_laptop.name} and price is {my_laptop.price}')        

print(my_laptop.new_laptop())