# #1 WAP to accept string from user find length of string with and without length function.

# # Using Length Function
str1 = input("Enter A String : ")
print(str1)
print(f'Length Of {str1} is : {len(str1)}')
print("Length Of", str1, "is : ", len(str1))


# # without length function

# str = input("Enter A String : ")

# count = 0
# for i in str:
#     count+=1
# print(count)    




# #2 WAP for accepting n from user check wether it is primt or not

# num = int(input("Enter Number To Check Prime or Not : "))

# count=0
# for i in range(1,num+1):
#     if num % i == 0:
#         count+=1
# if count > 2:
#     print(f'{num} Not Prime Number')        
# else:
#     print(f'{num} Prime Number')        





# # 3 WAP for accepting n from user find its factorial

# n = int(input("Enter Number To Find Factorial : "))
# fact = 1
# for j in range(1,n+1):
#     fact*=j
# print(fact)     



# # 4 WAP for printing fibonacci series
# [,0,1,1,2,3,5,8,13,21,34,55,89,114]

# a,b = 0,1
# new_list=[]
# new_list.append(a)
# new_list.append(b)

# for i in range(1,11):
#     c=a+b
#     new_list.append(c)

#     a=b
#     b=c
# print(new_list)    




# # 5 WAP to print all even no from 1 to 10

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)



# # 6 WAP for swapping of 2 variable

# a=10
# b=20
# print(f'a:{a},b:{b}')

# # a,b=b,a
# # print(f'a:{a},b:{b}')

# a=a+b
# b=a-b
# a=a-b
# print(f'a:{a},b:{b}')





# 7 WAP to disply following pattern
'''
*
**
***
****
*****
'''
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# # 8 check palindrome string

# string = "radar"
# r_string = string[::-1]
# if string == r_string:
#     print("Palindrome")
# else:
#     print("Not Palindrome")    



# WAP to remove dublicate element from given string

# s="ashitosh"
# s1=""
# for i in s:
#     if i not in s1:
#         s1+=i
# print(s1)        
         

# a="ashu"
# print(a.upper())         


print(ord('A'))
print(chr(98))