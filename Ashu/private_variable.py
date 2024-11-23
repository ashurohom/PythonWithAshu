class Bank:
    def __init__(self,AccNo,AadharNo):
        self.__AccNo=AccNo
        self.__AadharNo=AadharNo

    def Display(self):
        print(f"Account No : {self.__AccNo}")    
        print(f"Aadhar No : {self.__AadharNo}")  

    def GetAccountNo(self):
        return f'{self.__AccNo}'

    def GetAadharNo(self):
              return f'{self.__AadharNo}'             

details = Bank(10024,1111)
details.Display()

# print(details.__AccNo)        #error bcz private variable
# print(details.__AadharNo)

print(details.GetAccountNo())
print(details.GetAadharNo())