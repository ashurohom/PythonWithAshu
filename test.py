# a=1234

# a=(str(a)[::-1])
# print(int(a))


# def ReverseString(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return ReverseString(s[1:])+s[0]
# s = input("Enter number : "))    
# ReverseString(s)
# print(f'{s} : {ReverseString(s)}')

# class Stud:
#     name = "Ashu"
#     RollNo = 111
# s = Stud();
# print(s.name)
# print(s.RollNo)

# print("----------------------------")
# class Person:
#     def __init__(self,name):
#         self.name=name

# p1 = Person('Ashu')        
# print(p1.name)

# num=int(input("Enter Number : "))
# count=0
# if num % 2 == 0:
#     count+=num

# if count > 2:
#     print("Not Prime Number")    
# else:
#     print("Prime Number")    

# Print Prime Number Between 1 to 100

# n=11
# count=0
# if n % 2 == 0:
#     count+=n

# if count > 2:
#     print("Not Prime Number")    
# else:
#     print("Prime Number")        
        


# for i in range(2,26):
#     for j in range(2,i):
#         if i%j == 0:
#             break;
#     else:
#         print(i,end=" ")        




# Print the last second or highest second number from the list

list = [1,2,3,4,5,6,7,8,9,10]
list1 = [51,10,78,20,88,42,30]
number=list1[0]

for i in list1:
    if i > number:
        number=i

print(f"Highest Number : {number}")       


 
list2 = [25,87,33,10,55,15,100,20]
lowestNum = list2[0]
secondNum = list2[0]

for j in list2:
    if j < lowestNum:
        lowestNum=j

for j in list2:
    if j > lowestNum and (secondNum == lowestNum or j < secondNum):
        secondNum = j

print(f"Lowest Number : {lowestNum}")        
print(f"Second Number : {secondNum}")        
    