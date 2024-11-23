'''
Bank Account Management
Create a class BankAccount with attributes:

Account holder's name
Balance
Add methods to:

Deposit money
Withdraw money
Display the current balance
'''
class BankAccount:
    def __init__(self,AccountHolder,Balance):
        self.AccountHolder=AccountHolder
        self.Balance=Balance


    def Deposit(self,amount):
        if amount > 0:
            self.Balance += amount
            print(f'{amount} Deposited, New Balance {self.Balance}')    
        else:
            print(f'Invalid Ammount')    


    def Withdraw(self,amount):
        if amount > 0 and amount <= self.Balance:
            self.Balance -= amount
            print(f'{amount} Widhdrawn, Current Balance {self.Balance}')
        else:
            print(f'Invalid Amount Or Insufficient Balance')    


    def Display(self):
        print(f'Account Holder : {self.AccountHolder}')
        print(f'Current Balance : {self.Balance}')

account = BankAccount("Ashu",500)
account.Deposit(300)
account.Withdraw(200)
account.Display()         
