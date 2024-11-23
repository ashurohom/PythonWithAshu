# function is block of code defined with a name
# function is block of code that perform a specific task
# function usedd to overcome(down) the redundence 
'''
1) pre-defined / built-in function
2) user define function

def function_name(parameter1,parameter2,...):       //create function
    #some code                                      //function body
    return val
function_name(argument1,argument2,...)              //function call
'''

# addition

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(2,3)       #5
calc_sum(10,20)     #30
calc_sum(90,10)     #100


 
def sum(c,d):
    return c+d
mysum=sum(5,5)
print(mysum)


def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print('Avg : ',avg)
    return avg
calc_avg(98,68,85)