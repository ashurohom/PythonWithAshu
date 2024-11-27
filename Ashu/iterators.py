#iterators

l = [1,2,3,4,5]

a = iter(l)
print(a.__next__())
print(a.__next__())
print(next(a))


#genrators

def topten():

    yield 10
    yield 20
    yield 30
    yield 40

value=topten()    
print(value.__next__())

for i in value:
    print(i)    



def count_up_to(n):
    count = 1
    while count <= n:
        yield count  
        count += 1

# Create a generator
counter = count_up_to(5)

# Use the generator
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
# and so on...
