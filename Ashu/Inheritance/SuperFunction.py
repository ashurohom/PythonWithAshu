class One:
    def OneClass(self):
        return 'GHTechnology'
    
class Two(One):
    def TwoClass(self):
        a=super().OneClass()    
        print(f'Company Name {a}')
t1=Two()
t1.TwoClass()
