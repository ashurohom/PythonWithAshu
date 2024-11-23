a=10
b=0
# c=a/b
# print(c)

# Error : ZeroDivisionError: division by zero

# try:
#     x=10
#     y=0
#     z=x/y
#     print(z)
# except:
#     print("Can't Divide with zero, provide another number")    



# try:
#     a=int(input("Enter Number 1 : "))
#     b=int(input("Enter Number 2 : "))
#     c=a/b
#     print(c)
# except ValueError:
#     print("Enter Integer Value")

# except ZeroDivisionError:
#     print("Can't divide with zero")        



# Handle multiple exceptions with a single except clause

# try:
#      a=int(input("Enter Number 1 : "))
#      b=int(input("Enter Number 2 : "))
#      c=a/b
#      print(c)
# except(ValueError,ZeroDivisionError):
#      print("Enter Valid Value")    


# Using try with else clause

try:
    a=int(input("Enter Number 1 : "))
    b=int(input("Enter Number 2 : "))
    c=a/b
    print(c)
    
except ZeroDivisionError:
    print("can't divide by zero")    

else:
    print("In the else part")    