# print even number from the given list

list=[1,2,3,4,54,6,7,8,99,10]

# for i in range(0,10,2)
# if i%2==0:
#     print(i)


# for i in list:
#     if i % 2 ==0:
#         print(i)


s="deepak"
# print(s[2])


l=len(s)
for i in range(l):
    print(s[i],end="")
     


# Code Your Choice
 #odd number 
s=[1,2,3,4,5,6,7,8,9,10]
# for i in s:
#     if 1 % 2 !=0:
#     print(i)


for i in s:
    if i % 2 != 0:
        print(i)

print()

for i in s:
    if i % 2 == 0:
        continue
    else:
        print(i)     

# WAP to swap two number using two variable

a=10
b=20
print(f'a:{a}  b:{b}')


# using third variable

c=a
a=b
b=c
print(f'a:{a}  b:{b}')


# using two variable

a=a+b #30
b=a-b #10
a=a-b #20
print(f'a:{a}  b:{b}')







