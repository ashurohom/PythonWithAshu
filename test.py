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

n=25;

for i in range(2,n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")



        
        
