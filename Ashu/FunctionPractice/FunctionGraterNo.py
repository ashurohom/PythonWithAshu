'''
2. Create a function that takes a list of numbers as input and returns the largest number in the list.

Use a loop to find the largest number.
Example:
Input: [2, 8, 1, 7, 5]
Output: 8
'''

input = [2, 8, 1, 7, 5]

def GraterNo(input):
    no=input[0]

    for i in input:
        if i>no:
            no=i
    print(no)

GraterNo(input)    
