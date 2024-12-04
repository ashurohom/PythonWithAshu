class Public:
    def __init__(self,name):
        self.name=name
        print(f'Get Value : {self.name}')
    def setter(self):
        self.name = "Ashitosh"
        return self.name
    
obj = Public("Ashu")
print(f'Set Value : {obj.setter()}')
