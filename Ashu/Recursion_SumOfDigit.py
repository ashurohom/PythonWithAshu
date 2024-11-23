def SumOfDigit(n):
    if n < 10:
        return n
    else:
        return n%10 + SumOfDigit(n//10)
    
num = int(input("Enter Number : "))    
SumOfDigit(num)
print(f'Sum of {num} is {SumOfDigit(num)}')