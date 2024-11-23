class MySelf:
    def __init__(self,name):
        self.name=name

    def Display(self):
        print(f'{self.name}')    

    def __del__(self):
        print(f'Destructor Called...!')    

Self=MySelf("Ashu")        
Self.Display()
