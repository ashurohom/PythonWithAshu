# find the lowest and second lowest number from the list

list = [50,22,48,27,32,18]
lowestNum = list[0]

for i in list:
    if i < lowestNum:
        lowestNum=i
print(lowestNum)        