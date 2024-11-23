my_set = {2,4,6,8,"Ashu",12.5}
print(my_set,type(my_set))

print("Length : ",len(my_set))

my_set.update([10,20])
print("Update : ",my_set)

my_set2 = my_set.copy()
print("Copy : ",my_set2)

my_set.remove(20)
print("Remove 20 : ",my_set)

# my_set.remove(200)
# print("Remove Not Present 200 : ",my_set)

my_set.discard(200)
print("Remove Not Present 200 : ",my_set)


# Difference

x={1,2,3,4}
y={3,4,5,6}
print(x.difference(y))

# symmetric difference

print(x.symmetric_difference(y))


# Membership Operators : 

a = {1,2,3,4,5}
b = 2
print("Membership : ",b in a)
c = 10
print("Membership : ",c not in a)

# identity Operators

print("Identity : ",b is a )
print("Identity : ",b is not a )