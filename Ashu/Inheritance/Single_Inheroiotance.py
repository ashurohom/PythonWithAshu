class Company:
    def names(self):
        print(f'Company Name Is Mahindra')

class Product(Company):
    def products(self):
        print(f'Production is Car and Tractos')        

pro = Product() 
pro.names()
pro.products()       