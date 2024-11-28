'''
Question 2: Bank Account System
Create a class named BankAccount with the following features:

Attributes:
account_number: An integer representing the account number.
holder_name: A string for the account holder's name.
balance: A float representing the account balance.
Methods:
deposit(amount): Increases the balance by amount.
withdraw(amount): Decreases the balance by amount if sufficient balance exists. Otherwise, print an error message.
display_balance(): Displays the current balance.
Task:
Create an object of BankAccount with a starting balance of ₹10,000.
Perform the following operations:
Deposit ₹5,000.
Withdraw ₹3,000.
Attempt to withdraw ₹15,000.
Display the final balance.
'''

class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance

        
    def deposite(self,deposit):
        self.balance += deposit
        print(f"Amount ₹{deposit} has been deposited into your account No {self.acc_no}.")
        print(f'Current Balance Is {self.balance}\n')

    
    def withdraw(self,withdraw):
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Amount ₹{withdraw} has been withdrawn from your account No {self.acc_no}.")
            print(f'Current Balance Is {self.balance}\n')

        else:
            print(f"Insufficient balance! Cannot withdraw ₹{withdraw} from account No {self.acc_no}.")

    def display_balance(self):
        print(f'Acc No : {self.acc_no}')
        print(f'Name : {self.name}')
        print(f'Balance : {self.balance}\n')


bank = BankAccount(123,"Ashitosh",5000)
bank.display_balance() 
bank.deposite(2000)
bank.withdraw(1000)
  
