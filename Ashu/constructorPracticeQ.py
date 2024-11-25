''' Question:

In Python, explain the role of the constructor (__init__) and destructor (__del__) methods. Write a Python class Car that:

Has an __init__ method that initializes the car's make and model.
Has a __del__ method that prints a message when an object of the Car class is deleted.
Create an instance of the Car class inside a function, then delete the object manually and observe the output.
Provide the Python code and explain what happens when the object is created and deleted. '''

class Car:
    def __init__(self,year,model):
        self.year=year
        self.model=model

    def Show(self):
        print(f'{self.year} {self.model}')    

    def __del__(self):
        print("Execution End Sucessfully...!")    

MyCar = Car(2024,'TATA Harier')
MyCar.Show()

del MyCar

