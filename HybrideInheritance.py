#Hybride Inheritance

class A:
    def aee(self):
        print(f'Class A')

class B(A):
    def bee(self):
        print(f'Class B') 

class C(A):
    def cee(self):
        print(f'Class C')

class D(B,C):
    def dee(self):
        print(f'Class D')

obj = D()
obj.aee()                               
obj.bee()                               
obj.cee()                               
obj.dee()                               