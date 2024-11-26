'''
1. Write a function to calculate the factorial of a given number.

The function should take an integer as input and return the factorial of that number.
Example:
Input: 5
Output: 120
'''

def fact(value):
    a=1
    for i in range(1,value+1):
        a*=i
    return a
print(fact(5))    