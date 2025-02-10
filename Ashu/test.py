'''
Factorial
fibonacci series
palindrome
anagram
armstrong number
prime number
reverse number
swap key, value in dictionary
regullar expression
'''

# dict1 = {'A':1,'B':2,"C":3}
# # print(dict1)   
# dict2 = dict([(value, key) for key, value in dict1.items()])

# print(dict2)



import re
# num = '9527230560'
# a = re.fullmatch('[a-z][0-9]{9}',str(num))
# # pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if a is None:
#     print("Invalid Number")
# else:
#     print("Valid Number")


# mail = 'ashu.rohom@gmail.com'
# a = re.fullmatch(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}',mail)
# # a = re.fullmatch(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}', mail)
# if a is None:
#     print("Invalid mail")
# else:
#     print("Valid mail")





# dict1={"a":1,"b":2}
# print(dict1)
# dict2=dict1.pop('a')
# print(dict2)

# tup = ((2,5,7),(4,2,6),(9,8,1),(12,10,14)) 
# count = 0
# tlen = len(tup)
# for i in range(tlen):
#     if tup[i][0]%2 == 0 and tup[i][1]%2==0 and tup[i][2]%2==0:
#         count+=1
# print(count)        

# l=[]
# for i in range(1,51):
#     l.append(i*i)
# s=tuple(l)
# print(s)    

# print("***************")

# t = [i**2 for i in range(1,51)]
# print(t)



arr = [9,2,8,7,6,3,5,4,1]
print(arr)
arr.sort()

list=[]

for i in arr:
    if i % 2 == 0:
        print(i,end="")
    else:
        print(i,end="")
print()
print("--------------------------------------")     

arr = [9, 2, 8, 7, 6, 3, 5, 4, 1]

# Sort the list
arr.sort()

# Separate even and odd numbers
even_numbers = [num for num in arr if num % 2 == 0]
odd_numbers = [num for num in arr if num % 2 != 0]

# Arrange in the desired sequence
result = []
max_len = max(len(even_numbers), len(odd_numbers))

for i in range(max_len):
    if i < len(even_numbers):
        result.append(even_numbers[i])
    if i < len(odd_numbers):
        result.append(odd_numbers[i])

# Print the result
print(result)
