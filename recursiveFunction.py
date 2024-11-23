# Recursion factorial



def fact(n):
    if(n ==1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
print('fact:',fact(5)) 



def fact(num):
    c=1
    for i in range(1,num+1):
        c*=i
    print(c)   
    return fact 
fact(5)    



# Class Method

def factorial(num):
    if num==0:
        result=1
    else:
        result = num*factorial(num-1)
    return result

print(f'Factorial : {factorial(5)}')


