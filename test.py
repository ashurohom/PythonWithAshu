# Print highest and second highest number from the list

# list = [20,98,24,36,75,88,12,45]
# highNum = list[0]
# secondHigh = list[0]

# for i in list:
#     if i > highNum:
#         highNum=i

# for i in list:
#     if i < highNum and(highNum == secondHigh or i > secondHigh):
#         secondHigh=i

# print("Highest Num : ",highNum)    
# print("Second High Num : ",secondHigh)    


# # Print the factorial of given number

# num=int(input("Enter Number For Factorial : "))
# fact=1

# for i in range(1,num+1):
#     fact*=i
# print(f'{num}! = {fact}')    



# Armstrong Number

number = 153

digit = [int(d) for d in str(number)]
l=len(digit)

arm = sum(d ** l for d in digit)

if arm == number:
    print(f'{number} Is Armstrong Number')
else:
    print(f'{number} Is Not Armstrong Number')
    
    