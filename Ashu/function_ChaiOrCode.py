# syntax
'''
def fun_name(parameter): //create function
     Statment
     Statment
     Statment
    return          // return value
fun_name(arguments)  //function call
'''


# Example 1

def square(number):
    return number ** 2
    
result = square(5)
print(f'square is {result}')

# Function with multiple parameter

def add(num1,num2):
    return num1+num2
print(f'Addition {add(5,5)}')


# Polymorphism in Function

def mul(num1,num2):
    return num1*num2
print(f'Multiplication {mul(5,5)}')
print(f'Multiplication {mul(5,'a')}')
print(f'Multiplication {mul('a',5)}')

# Function return multiple value
# create function that return area and circumference of circle


import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area,circumference

a,b = circle(4)
print(f'Area {a}   Circumference {b}')
print(f'Area {round(a)}   Circumference {round(b)}')

# Default Parameter

def greet(name="User"):
    return f"Hello {name} !"
print(greet())
print(greet("Ashu"))


# lambda function

cube = lambda x:x ** 3
print(cube(3))
newcube = cube
print(newcube(5))

add = lambda a,b:a+b
print(add(2,2))

# find cube using list co prehirision
list = [2,3,4]
mycube = [x**3 for x in list]
print(mycube)

# function with arguments

def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
print(sum_all(1,2,3,4,5,6,7,8,9,10))

# keywords arguments

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

print_kwargs(name="Ashu")        
print_kwargs(name="Ashu",rollno="111",clg="Sanjivani COE")  


# genrate function with yield

def even(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even(10):
    print(num)        


# Recursive Function

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
print(fact(5))            