'''
5. Create a Simple Calculator
Write a function named calculator(a, b, operator) that takes two numbers (a and b) and a string operator (+, -, *, /) and returns the result of the operation.
Example:

python
Copy code
print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '*'))  # Output: 50
'''

def calculator(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    
    elif op == '*':
        return a*b
    
    elif op == '/':
        return a/b
    else:
        return "Invalid Operator"
print(calculator(5,5,'+'))    
