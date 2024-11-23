'''
Set
set is colletion of unordered items.
unordered
unique(no dublicate)
immutable
{}
hetrogenious are allowed
'''

# mydict = {}  // empty dictionary


# empty set
myset = set()
print(type(myset))

set = {1,2,3,"ashu","rohom",12.25}

# methods in set

# 1) add

set.add(4)
set.add((7,8,9))
set.add("hello krishna")
print(set)

# 2) remove

set.remove(4)
print(set)

# 3) clear

# set.clear()
# print(len(set))

# 4) pop
print("-----------")
print(set.pop())


# 5) union : remove dublicatr value and return new set

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #{1,2,3.4}

set3 = {'Ashitosh','Baban','Rohom'}
set4 = {'Ashitosh','Rohom','Patil'}

print(set3.union(set4))


# intersection : return common value

print(set1.intersection(set2))  #{2, 3}
print(set3.intersection(set4))  # {'Rohom', 'Ashitosh'}