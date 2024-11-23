# tuple

tuple = (1,2,3,4,5)
print(tuple)
print(type(tuple))

# tuple are immutable
# in tuple add single value with comma always
# tuple = (1,) - datatype : tuple
# tuple = (1) - datatype : integer 

# indexcing / slicing
print(tuple[2])
print(tuple[1:4])
print(tuple[::-1])

# length
print(len(tuple))

# concat

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)

t3 = (t1,t2)
print(t3)
print(len(t3))

t4 = t1+t2
print(len(t4))

# count

t5 = (1,2,3,1,5,1,4,1)
print(t5.count(1))