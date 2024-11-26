# without lambda

def sqr(num):
    return num*num
print(sqr(13))


# with lambda

squr = lambda x:x*x
print(squr(15))


# addition

sum1 = lambda a,b:a+b
print(sum1(5,5))


# grater number

def grater(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

print(grater(10,20,15))


# grater number using lambda

g = lambda a,b,c:a if a>b and a>c  else  b  if b>c else c
print(g(5,7,3))


a=100
b=200