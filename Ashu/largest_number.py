# Problem: Write a Python program that takes a list of numbers as input from the user and finds the largest number in the list.?

list = [10,100,50,30,90,20,40]
grater_num = list[0]

for i in list:
    if i > grater_num:
        grater_num = i
print(grater_num)
