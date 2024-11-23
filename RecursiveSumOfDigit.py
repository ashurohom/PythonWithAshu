
def SumOfDigit(n):
    if n < 10:
        return n
    else:
        return n%10 + SumOfDigit(n//10)
n=int(input("Enter Number : "))
SumOfDigit(n)
print(f'Sum Of {n} Is {SumOfDigit(n)}')

