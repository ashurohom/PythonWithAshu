# Write a python program to find sum of odd values from the given list.

list = [2,4,5,7,8,9,3]
sum = 0
for i in list:
    if i % 2 != 0:
        sum+=i
print(f'Sum Of Odd Value {sum}')        