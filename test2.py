# find the lowest and second lowest number from the list

list = [50,22,48,27,32,18]
lowestNum = list[0]
secondLowest = list[0]

for i in list:
    if i < lowestNum:
        lowestNum=i

for i in list:
    if i > lowestNum and (secondLowest == lowestNum or i < secondLowest): 
        secondLowest=i
print(lowestNum)        
print(secondLowest)


print("********************************")



list2 = [50,22,48,27,32,18]
highestNum = list2[0]
secondHigh = list2[0]

for i in list2:
    if i > highestNum:
        highestNum = i

for i in list2:
    if i < highestNum and (secondHigh == highestNum or i > secondHigh):
        secondHigh = i

print(f"highest Number : {highestNum}")        
print(f"Second High : {secondHigh}")

