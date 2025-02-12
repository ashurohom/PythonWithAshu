# find the lowest and second lowest number from the list

list = [50,22,48,27,32,18]
lowestNum = list[0]
secondLowest = list[0]

for i in list:
    if i < lowestNum:
        lowestNum=i

for i in list:
    if i > secondLowest and (secondLowest == lowestNum or i < secondLowest): 
        secondLowest=i
print(lowestNum)        
