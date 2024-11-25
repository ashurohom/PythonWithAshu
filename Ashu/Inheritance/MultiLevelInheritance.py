class One:
    def OneClass(self):
        print("Inside One Class")

class Two(One):
    def TwoClass(self):
        print("Inside Two Class")

class Three(Two):
    def ThreeClass(self):
        print("Inside Three Class")

class Four(Three):
    def FourClass(self):
        print("Inside Four Class")
        
            

f = Four()
f.OneClass()
f.TwoClass()
f.ThreeClass()                     
f.FourClass()