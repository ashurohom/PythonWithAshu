#Logical Operators

#Logical AND
a=10
b=5
'''
print(a>5 and a<20)     #True
print(a>5 and a>20)     #Flase
print(a>=10 and a<b)    #False


#Logical OR

print(a>=10 or a<b)     #True
print(a>=10 or a<b)     #True
print(a>11 or a<b)      #False

#Assignment Operators

a=10
a=a+10
print(a)

a-=5
print(a)

a+=5
print(a)

a*=5
print(a)

a/=5
print(a)

a//=5
print(a)

a**=5
print(a)

a!=5
print(a)



#Ternary Operator

a=50
b=15
c=20
x = 10 if a>b else b
#print(x)

y = 10 if a<b else b
#print(y)


z = a if a>b else b  if a>c else c
print(z)
zz = a if a>b and a>c else b if b>c else c
print(zz) 



#input

a = input("Enter Name  :")
print(a)

b = eval(input("Enter Number/string : "))
print(b)

c = int(input("Enter Num1  :"))
d = int(input("Enter Num2  :"))
print(c," + ",d," = ",c+d)
'''

#Type Casting

# m=50
# print(m,type(m))
# n=(float(m))
# print(n,type(n))

# print(2**3**2)

# a=4
# b=11
# print(a | b)
# print(a >> 2)

# y=10
# x=y+=2
# print(x)

# x=10
# y=50
# if x ** 2 > 100 and y < 100:
#     print(x,y)

# print(2*3**3*4)

# x=100
# y=50
# print(x and y)

# print(type({}) is set) : #False


