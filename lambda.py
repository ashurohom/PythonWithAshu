# filteer()

l=[1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    if n%2==0:
        return True
    
x = list(filter(is_even,l))
print(x)

y = list(filter(lambda i:i%2==0,l))
print(y)

z = list(filter(lambda i:i%2!=0,l))
print(z)


# map()

sq = list(map(lambda n:n*n,l))
print(sq)

qb = list(map(lambda n:n**3,l))
print(qb)

# Using Function
def sq(n):
    return n*n

sqr = list(map(sq,l))
print(sqr)

# Reduce

from functools import reduce

s = reduce(lambda x,y:x+y,l)
print(f'Addition : {s}')


def fun1():
    s1=10
    return 'hii'
print(fun1())
# print(s1)

import lambda_function
print(lambda_function.a)