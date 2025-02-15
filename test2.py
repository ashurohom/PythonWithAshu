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





# Print the factorial of given number

num=int(input("Enter Number For Factorial : "))
fact=1

for i in range(1,num+1):
    fact*=i
print(f'{num}! = {fact}')    




# Armstrong Number

number = 153

digit = [int(d) for d in str(number)]
l=len(digit)

arm = sum(d ** l for d in digit)

if arm == number:
    print(f'{number} Is Armstrong Number')
else:
    print(f'{number} Is Not Armstrong Number')


# Length Of String

str = "Ashitosh"

l =len(str)
print(f'Length Of {str} Is : {l}') 

count=0
for i in str:
    count+=1
print(f'Length Of {str} Is : {count}') 



#8 WAP For Print Fibonacci Series

a=0
b=1
series = []
series.append(a)
series.append(b)

for i in range(1,11):
    c=a+b
    series.append(c)

    a=b
    b=c

print(series) 


#9 Swap Two Number With or Without Third Variable

a=10
b=20

# c=a
# a=b
# b=c
# print(a,b)   

a=a+b
b=a-b
a=a-b
print(a,b)



#10 Convert Number into its Corresponding String [1:one]

dict = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine",
}

num = int(input("Enter Number : "))
print(f'{num} : {dict[num]}')