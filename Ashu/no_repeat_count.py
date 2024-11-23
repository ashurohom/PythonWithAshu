# Write a program to check frequency of occurrence of 4 in the given list.

l=[2,4,5,6,2,3,8,2,4,5,10,2,1,5]

n = int(input("Enter Number : "))
count = 0

if n in l:
    for i in l:
        if i == n:
            count += 1
    print(f'Count of {n} is : {count}')        
else:
    print(f'{n} Not Present In List')                 