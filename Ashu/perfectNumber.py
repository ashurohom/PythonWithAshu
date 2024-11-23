# Write a program to check whether a number is a perfect number or not.
# Example : Perfect Number [6, 28, 496, 8128]

'''
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself). For example, 
6 is a perfect number because its divisors are 1,2,3, and their sum is 
1+2+3=6.

Steps to Check if a Number is Perfect:
1) Find all the divisors of the number (excluding the number itself).
2) Add the divisors.
3) If the sum equals the original number, it is a perfect number.
'''

num = int(input("Enter Number TO Check No Is Perfect No or Not : "))
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum+=i 

if num == sum:
    print(f'{num} is Perfect Number')
else:
        print(f'{num} is Not Perfect Number')    