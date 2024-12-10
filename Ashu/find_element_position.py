#Python Code
# Write a python program to find the position of first occurrence of a given element assigned to variable n in the given list l.

l=[10,2,3,11,15,6,7,15,20]
n=15

for i in range(len(l)):
    if l[i] == n:
        print(f'{n} index is {i}')
        break
