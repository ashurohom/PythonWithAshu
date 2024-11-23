# marks=[90.5,68,85.5,98,55]
# student=['ashu',25,88.90,'A']
# print(student)
# print(type(student))

mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
print(len(mylist))

print(mylist[0:5])
print(mylist[3:10])
print(mylist[::-1])
print(mylist[-1:-6:-1])
print(mylist[1::2])

# append : add one element at the end
list = [1,3,2,6,5,4]
list.append(7)
print(list)

# sorting
print(list.append(8))   #return none it will direct chage in list
print(list.sort())      ##return none it will direct chage in list
print(list)

list.sort(reverse=True)
print(list)


# sorting on string

charlist = ['c','a','d','b','e']
print(charlist.sort())
print(charlist)
print(charlist.sort(reverse=True))
print(charlist)

# reverse  : directly reversed a main string
print("-------------")
charlist1 = ['c','a','d','b','e']
charlist1.reverse()
print(charlist1)

# insert : insert a value at specific location

charlist2 = ['c','a','d','b','e']
charlist2.insert(2,'c')
print(charlist2)


# remove : to remove first occurrence of element

charlist2.remove('c')
print(charlist2)

charlist2.pop(4)
print(charlist2)

print(charlist2.count('c'))
