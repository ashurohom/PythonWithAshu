'''
Default Constructor
Create a class Car with attributes brand and color.
Use a default constructor to initialize them with "Unknown" values. Add a method to display the car details.
'''

# class Car:
#     brand = "mahindra"
#     color = "white"

#     def CarDetail(self):
#         print(f'{self.brand} {self.color}')    

# c1 = Car()
# c1.CarDetail()        


class Cars:
    def __init__(self,brand="Mahindra",color="White"):
        self.brand=brand
        self.color=color

    def CarDetails(self):
            print(f'{self.brand} {self.color}')
c1=Cars()      
c1.CarDetails()      

            