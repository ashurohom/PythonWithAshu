# # find

# a="rashu@radha"
# print(a.find('@')) #5
# print(a.find('m')) # print the -1 value

# # index
# print(a.index('@')) #5
# print(a.index('m')) # it will give value error


# count

# name = "ashitoshrohom"
# count = 0

# for i in name:
#     if i == 'o':
#         count+=1
# print("o : ",count)



# # replace old string to new string
# # we can change a word also
#  a="ashu"
# print(a)
# print(a.replace('a','s'))

# # length()
# print(len(a))

# s1="ashitosh"
# print(s1)

# s2=(s1.replace('a','s'))
# print(s2)


# # splitting of string

# a1="ashibtosh"
# a2=a1.split('b')
# print(a2)

# a3="My Name Is AShitosh"
# a4=a3.split(' ')
# print(a4)

# Join of string
#s=seperator,join(group of string)

# l1=('Ashu','Rohom','Patil')
# l2=' '.join(l1)
# print(l1)
# print(l2)


# changing case of a seting

# string1 = "Hello, My name is Ashitosh"

# print(string1.upper())
# print(string1.lower())
# print(string1.swapcase())
# print(string1.title())
# print(string1.capitalize())




# 9)checking starting and ending part of the string

# s11 = "Python"
# print(s11.startswith('P'))  #True
# print(s11.endswith('n'))  #True


# To check type of character in string

# print('ashu123'.isalnum())
# print('ashu123'.isalnum())
# print('ashu123'.isalpha())
# print('ashu123'.isdigit())
# print(' '.isspace())


# Q. wap to add or addition of numbers present in a given string
'''
s = "ashu1111"
a = 0

for i in s:
    if i.isdigit():
        a+=int(i)
print(a)        
'''


# # a4b3c2d1
# # op : aaaabbbccd 
# s = "a1s2u3"
# s1 = ''
# b = ""

# for i in s:
#     if i.isalpha():
#         # s1=s1+i
#         p=i
#     elif i.isdigit():
#         s1=s1+(p*(int(i)))    
# print(s1)        




# or

# s = "a1s2u3"
# s1 = ''
# b = ""

# for i in s:
#     if i.isalpha():
#         s1=s1+i
#         p=i
#     elif i.isdigit():
#         s1=s1+(p*(int(i)-1))    
# print(s1)        



# s='a4k3p2'
# op : aeknpr


