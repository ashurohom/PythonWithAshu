#Multiple INHERITANCE

class A:
    def aee(self):
        print("Class A")
class B:
    def bee(self):
        print("Class B")
class C:
    def cee(self):
        print("Class C")
class D(A,B,C):
    def dee(self):
        print("Class D")

obj = D()
obj.aee()
obj.bee()
obj.cee()
obj.dee()        