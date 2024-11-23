'''
A lambda function is a small, anonymous function defined using the lambda keyword. 
It is typically used for short, single-use functions, especially in scenarios where 
a full function definition is not necessary.


'''

# lambda function

sqr = lambda x: x*x
print(sqr(2))
print(sqr(5))
print(sqr(10))

cube = lambda a:a*a*a
print(cube(2))
print(cube(3))
print(cube(4))

add = lambda x,y:x+y
print(add(4,4))

a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))

avg = lambda a,b:(a+b)//2
print(avg(a,b))


# lambda with no arguments

greet = lambda: "Radhe Krishna"
print(greet())

# lambda with conditionals

is_even = lambda x: 'Even' if x%2 == 0 else 'Odd'
print(is_even(10))
print(is_even(11))


# Program for even number with a lambda function
l = [10, 5, 12, 78, 6, 1, 7, 9]
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are: ", even_nos)



# Filter

l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_nos = list(filter(lambda x: x > 0, l))
print("Positive numbers are: ", positive_nos)


# map

list1 = [2, 3, 4, 8, 9]
list2 = list(map(lambda x: x*x*x, list1))
print("Cube values are:", list2)


# reduce

from functools import reduce
list1 = [20, 13, 4, 8, 9]
add = reduce(lambda x, y: x+y, list1)
print("Addition of all list elements is : ", add)