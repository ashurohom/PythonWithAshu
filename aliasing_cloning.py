# Asiasing
'''Aliasing: Aliasing is when two or more variables point to the same object in memory. 
             Changing the object through one variable affects it for all other aliases'''

print("\n*** Asiasing ***")

list1 = [10,20,30,40]
print("Before List 1 : ",list1)

list2 = list1 
list2[1] = 200
print("After List 1 : ",list1)
print("After List 2 : ",list2)

print("Location : ",id(list1))
print("Location : ",id(list2))


# cloning
'''Cloning: Cloning is making an exact copy of an object in a new memory location. 
            Changes to the clone do not affect the original object.'''

print("\n*** cloning ***")

my_list1 = ['a','b','c','d']
print("Before my_list 1 :",my_list1)

my_list2 = my_list1[:]
my_list2[1] = 'e'
print("After my_list 1 : ",my_list1) 
print("After my_list 2 : ",my_list2) 

print("Location : ",id(my_list1))
print("Location : ",id(my_list2))