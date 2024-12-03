# Hierarchical Inheritance

class A:
    def aee(self):
        print(f'Class A')

class B(A):
    def bee(self):
        print(f'Class B')

class C(A):
    def cee(self):
        print(f'Class C')


obj1 = B()
obj1.aee()
obj1.bee()

obj = C()
obj.aee()
obj.cee()


