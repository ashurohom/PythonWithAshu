# import moduleuser

# mycity = moduleuser.city[0]
# print("MyCity : s",mycity)

# print(moduleuser.city)


# names = moduleuser.name[0:4]
# print(names)


# from moduleuser import *
# abc()


from random import *

#random
print(random())
for i in range(10):
    print(random())

#randint
print(randint(1111,9999))
for i in range(10):
    print(randint(51,100),end=" ")
print()

#uniform
print(uniform(100,999))    
for j in range(5):
    print(uniform(1000,9999),end=" ")
print()

#randrange
print(randrange(10))    
print(randrange(1,11))
print(randrange(1000,9999,2))

print()

#choice
list=['ashu','tejas','rani','sanket','pooja']
for i in range(1):
    print(choice(list))


