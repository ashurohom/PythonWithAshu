# List Comprehirson

list = [12,34,11,32,15]

x= [i==12 for i in list]
print(x)

y=[i%2==0 for i in list]
print(y)

z=[i for i in list if i%2==0]
print(z)

c=[i*i for i in list]
print(c)


# set

d = {i for i in range(1,11) if i%2==0}
print(d)