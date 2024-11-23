# range

for i in range(2,7,2):
    print(i)

print("-------------------------")

for j in range(5,-1,-1):
    print(j)    

print("-------------------------")


# indexing

name = "Ashitosh"
for k in range(len(name)):
    letter=name[k]
    print(k,"=",letter)

print("-------------------------")


# list

mylist = [1,2,3,4,5,6,7,8,9,10]

for x in range(len(mylist)):
    print(mylist[x])


print("-------------------------")


# range to reverse a list

list = ['ashu','pari','teja','vishu','rani']
for y in range(len(list)-1,-1,-1):
    print(list[y])

print("-------------------------")

# Decrementing range() using step    

for z in range(30,1,-3):
    print(z)

