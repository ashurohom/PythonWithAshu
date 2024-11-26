'''
5. Write a function that accepts a variable number of arguments and returns their average.

Use *args to handle a flexible number of inputs.
Example:
Input: average(4, 8, 15, 16, 23, 42)
Output: 18.0
'''

def avg(*num):  
    counts=len(num)
    add=0
    for i in num:
        add+=i

    return add/counts
print(avg(4,8,15,16,23,42))        