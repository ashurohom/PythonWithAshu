# Write a python program to find the minimum number in the given list.

list=[10,200,34,78,12,54]
min_num = list[0]

for i in list:
    if i < min_num:
        min_num=i
print(f'Minimum Number {min_num}')        


