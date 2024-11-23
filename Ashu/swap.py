# swap number without using third variable

x=100
y=200

x,y=y,x
print(x,y)

print("--------------------------------------")

a=10
b=20

# using addition
a=a+b
b=a-b
a=a-b

print(a,b)


print("--------------------------------------")

c=25
d=50

c=c*d
d=c//d
c=c//d

print(c,d)