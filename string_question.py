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



# s='a4k3p2'  # o/p : aeknpr  [a=97,k=107,p=112]
# a=""
# for i in s:
#     if i.isalpha():
#         a+=i
#         p=i
#     elif i.isdigit():
#         a=a+chr(ord(p)+(int(i)))
# print(a)            


# print(ord('s'))
# print(chr(101))


# Q.WAP to remove dublicate char in given string

s1 ="rohom"
a1=""
for i in s1:
    if i in a1:
        continue
    else:
        a1=a1+i
print(a1)



s ="rohom"
a=""
for i in s:
    if i not in a:
        a=a+i
       
print(a)

