# Recursion
# when a function call itself repeatedly.

def show(n):
    if(n == 0):     #base case
        return
    print(n)
    show(n-1)
show(5)    

'''
o/p 
5
4
3
2
1
'''



# factorial

def fact(n):
    if(n ==1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
print('fact:',fact(5))    