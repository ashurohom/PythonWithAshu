
def myfun():
    print("My First Functon Code")
myfun()

def myfun2():
    return("My Second Functon Code")
print(myfun2())


def add(a,b):
    c=a+b
    print("Add : ",c)
    return c
add(10,15)
    

def user(a,b):
    print(a,b)
    return a,b
user("Ashu","Rohom")



# waf to check whether the given number is odd or even

def evenodd(a):
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")
evenodd(2)            
evenodd(3)            


# waf to find factorial of given number

def fact(num):
    f=1
    for i in range(1,num+1):
        f*=i
    print(f)
    return f
fact(5)        


# default argument

def wish(name="Pahune"):
    print(f"hello,{name} Namskar")
wish("Ashu")    
wish()    


def myadd(b,a=10):
    c=a+b
    print("Addition:",c) 
    return c
myadd(5)
myadd(5,5)

# variable length
# when pass the *n = it consider as a tuple


def number(*num):
    total=0
    for i in num:
        total=total+i
    print("Addition : ",total)
    return total
number(5,4,3,2,1)

