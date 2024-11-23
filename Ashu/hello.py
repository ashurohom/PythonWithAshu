print("Hello Ashu,")

#Single Line Command 

'''
Multi 
Line
Command
'''

# name = "ashitosh"
# print("Name : ",name)

'''Addition
a=10
b=20
c=a+b
print(a,"+",b," = ",c)


#Input

# a = input("Enter Name : ")
# print("Name : ",a)

name = input("Enter Name : ")
print("Hello, ",name)

x=int(input("Enter A : "))
y=int(input("Enter B : "))
print(x,"+",y,"=",x+y)

#Input with datatype

a=input("Enter Rose Color : ")
b=int(input("Enter Rose Quantity : "))
c=float(input("Enter Rose Price : "))
print("Rose Color : ",a)
print("Rose Quantity : ",b)
print("Rose Price : ",c)


#datatype in python

#int
a = 5
print(a,type(a))

#string
ab = "RadheKrishna"
print("Wel-Come",ab,type(ab))

#float
abc = 155.15
print(abc,type(abc))

#complex
x = 2+3j
print(x,type(x))

#boolean
y=True
print(y,type(y))


#new line or multi line
print("WelCome To Python Programming Language \n My Name Is Ashitosh \n and i will teach you Python")

print("""WelCome To Python Programming Language
      My Name Is Ashitosh 
      and i will teach you Python""")


import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

a=10
print(type(a))

v='Ashu'
print(v,type(v))

w="Ashu"
print(w,type(v))


o = 10
p = 20
print(o,'+',p," = ",o+p)

a="ashu"
b="rohom"
print(a,'+',b," = ",a+b,end=" ")

c="Ashu"
d=10
print(c+d)



a=[1,2,3]
print(a)
print(type(a))

b=(1,2,3,4,5)
print(b)
print(type(b))


x=16**4
print(x)

'''

print(10 > 20)
print(10 >= 20)
print(10 < 20)
print(10 <= 20)