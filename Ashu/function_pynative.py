from random import randint
# Function

def msg():
    print("Wel-Come")
msg()    
       

# Creating a function with parameters

def student(name,course):
    print("Helllo",name,"WelCome to function body")
    print("Your course is : ",course)
student('ashu','python')    



# Creating a function with parameters and return value also call function

def addition(a,b):
    add = a + b
    print(a," + ",b," = ",add)
    return add
addition(15,5)


# odd even code using function

def even_odd(a):
    if a % 2 == 0:
        print(a," : Even Number")
    else:
        print(a," : Odd Number")    
even_odd(11)        
student('ashu','python')    

# random number
print(randint(1111,9999))



# Return Multiple Values

def math_operation(n1,n2):
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 // n2

    print(n1, '+', n2, '=',add)
    print(n1, '-', n2, '=',sub)
    print(n1, '*', n2, '=',mul)
    print(n1, '/', n2, '=',div)

    return add,sub,mul,div

math_operation(10,2)


# local and global variable

global_var = "namaste"

def check_variable():
    local_var = "hello"
    print(local_var)    #local variable
    print(global_var)   #not give error bcz flobal variable allow in local variable or function
check_variable()

# print(local_var)        #give error bcz the local variable is not accessible from outside of the function.
print(global_var)

print("-------------------------------------------")






# global keyword in function
x = 5

def first():
    print("First Function Value : ",x)

def second():
    x = 555     #modify global variable and function treat it as a local variable
    print("Second function value : ",x)

def third():
    print("third function value : ",x)    

first()
second()
third()    


# now use a globle keyword in function
print()
x = 5

def first():
    print("First Function Value : ",x)

def second():
    global x        # Modify global variable using global keyword
    x = 555         # now global variable value change s
    print("Second function value : ",x)

def third():
    print("third function value : ",x)    

first()
second()
third()  




# Variable-length Arguments

def additions(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Addition : ",total)
    return total

additions()
additions(1,2,3,4,5)    
additions(2,2,2,2,2)    