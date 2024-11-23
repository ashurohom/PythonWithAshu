class Employee:
    def __init__(self,name):
        self.name=name
        print(f'{self.name} is created...')

    def __del__(self):
        print(f"{self.name} is deleted...!")

NewEmployee=Employee("Ashitosh")        

# del NewEmployee  #Destructor Automatically Call,No Need to physically delete           