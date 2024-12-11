#Destructor

class A:
    def __init__(self,name):
        self.name=name
        print("Ashu")

    def display(self):
        return self.name   
    
    def __del__(self):
        print("Object Deleted")

obj = A("AshuRohom")    
print(obj.display())
# del obj 
print("After Object Delete")
#destructor call when object is deleted but vs code has issue
