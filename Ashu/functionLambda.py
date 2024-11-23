# Square
x = lambda x: x*x
# n=int(input("Enter Number : "))
# print(x(n))
print(f'Square {x(5)}')

# Addition
y = lambda a,b:a+b
print(f'Addition {y(10,5)}')
      

#Lambda In List

lists = [1,2,3,4,5]
z = list(map(lambda x:x*2,lists))
print(z)
