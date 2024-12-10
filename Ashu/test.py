# # List Comprehirson

# list = [12,34,11,32,15]

# x= [i==12 for i in list]
# print(x)

# y=[i%2==0 for i in list]
# print(y)

# z=[i for i in list if i%2==0]
# print(z)

# c=[i*i for i in list]
# print(c)


# set

# d = {i for i in range(1,11) if i%2==0}
# print(d)

x = 10.57
print(f'x : {x} & DataType : {type(x)}')
y=int(x)
print(f'y : {y} & DataType : {type(y)}')

list = ["ashu",111,True,11.11,3+4j]
print(list,":",type(list))

print()
dict = {"a":1, "b":2}
print(f'Original Dict : {dict}')

swapdict = {b:a for a, b in dict.items() }
print(f'Swap Dict : {swapdict}')
