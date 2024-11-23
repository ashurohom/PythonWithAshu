# import
import math
print(math.sqrt(5))         #2.23606797749979
print(math.pow(5,2))        #25.0
print(math.factorial(5))    #120

# import multiple module
import math,random
print(math.log(2))          #0.6931
print(random.randint(11,99))#12(random number)

# Import only specific classes or functions from a module
from math import factorial      # import only factorial function from math module
print(factorial(5))         #Not require module name


# Import with renaming a module/Aliasing
import random as rand
print(rand.randrange(10,20))


# import all names
from math import *
print(pow(4,2))
print(factorial(5))

print(pi*3)
print(sqrt(100))


# The dir() function
import math
print(dir(math))