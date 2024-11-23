'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
print("------------Square------------------")
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print("")    








'''
*
**
***
****
*****    
'''
print("------------Right Half------------------")
for a in range(1,n+1):
    for aa in range(1,a+1):
        print("*",end=" ")
    print("")   





'''
*****
****
***
**
*
'''
print("-----------Reverse Right Half-------------------")
m = 6
for b in range(m):
    for bb in range(b,m-1,):
        print("*",end=" ")
    print("")    







'''
    *
   **
  ***
 ****
*****          
'''    
print("-----------Left Half-------------------")

for c in range(5):
    for cc in range(5-c-1):
        print(" ",end=" ")
    for ccc in range(c+1):
        print("*",end=" ")
    print("")        








"""
*****
 ****
  ***
   **
    *
"""
print("-----------Reverse Left Half-------------------")

for d in range(5):
    for dd in range(d+1):
        print(" ",end=" ")
    for ddd in range(5-d):
        print("*",end=" ")
    print("")        





'''
*****
 *****
  *****
   *****
    *****
'''
print("-----------Rhombus Pattern-------------------")

for e in range(5):
    for ee in range(e+1):
        print(" ",end=" ")
    for eee in range(5):
        print("*",end=" ")
    print("")    