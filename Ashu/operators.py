# Arithmatic

a=25
b=20

# Addition
# print(a, " + " ,b, " = ",a+b)

# Substraction
# print(a, " - " ,b, " = ",a-b)

# Multiplication
# print(a, " * " ,b, " = ",a*b)

# Division
# print(a, " / " ,b, " = ",a/b)

# Remainder
# print(a, " % " ,b, " = ",a%b)

# Floor Devision
# print(a, " // " ,b, " = ",a//b)

# Expoinentioal(power)
# print(a, " ** " ,b, " = ",a**b)


# Comparison / Relational

p=30
q=20

# print(p>q)
# print(p>=q)
# print(p<q)
# print(p<=q)

r=20
s=25

# print(r>s)
# print(r>=s)
# print(r<s)
# print(r<=s)


# Logical 

a=10
b=20
c=30

# print(a<b and b<c)      #True
# print(a > b and b>c)    #False

# print(a < b or b>c)    #True
# print(a > b or b>c)    #False

x=a < b     
# print(not x)            #False



#Equality

v1 = 10
v2 = 10
v3 = 15

# print(v1 == v2)         #True
# print(v1 != v2)         #False


#Assignment

# a=10
# print(a)

#  a+=10            #a=a+10
# print(a)

# a-=10
# print(a)

#  a*=10
# print(a)

#  a/=10
# print(a)

#  a//=10
# print(a)

#  a**=10
# print(a)

#  a%=10
# print(a)


# ternary operator

a=20
b=50
c=35

# print("A = ",a, "B = ",b)

val = a if a>b else b 
# print("Grater No : ",val)

val1 = a if a<b else b 
# print("Lower No : ",val1)

val2 = a if a>b and a>c else b if b>c else c
# print("Grater No : ",val2)

val3 = a if a<b and a<c else b if b<c else c
# print("Lower No : ",val3)



# identity operator

aaa=10
bbb=10
print(aaa is bbb)
