# Write a python program to count the number of positive and negative values given in the list.

list = [10,5,-2,6,-9,9,4,7,-10]
count = 0
count2 = 0
for i in list:
    if i>=1:
        count+=1
    else:
        count2+=1    
print(f'Positive Value {count}')
print(f'Negative Value {count2}')        