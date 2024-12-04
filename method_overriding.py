class A:
    def name(self):
        print(f"Hello")

class B(A):
    def name(self):
        print(f'Welcome')

obj = B()
obj.name()        
