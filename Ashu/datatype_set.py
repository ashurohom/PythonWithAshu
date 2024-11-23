my_set = {1,2,3,4,5,6,7,8,9,0}
print(my_set)
print(type(my_set))

my_set.add(10)
print(my_set)

my_set.remove(6)
print(my_set)


new_set = frozenset(my_set)
print(new_set)

# new_set[1] = 3 
# print(new_set)        #Error


