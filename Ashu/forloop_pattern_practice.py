'''
0
2 4
6 8 10
12 14 16 18
'''

c=0
for i in range(1,6):
    for j in range(i):
        print(c,end=" ")
        c+=2
    print()    
print("---------------------")










'''
2
4 4
8 8 8
16 16 16 16
'''

d=2
for i in range(1,6):
    for j in range(i):
        print(d,end=" ")
    d*=2
    print()    
print("---------------------")









'''
*****
 ****
  ***
   **
    *
'''

num=5
for i in range(1,num+1):

    for j in range(1,i):
        print(" ",end=" ")
    
    for k in range(num-i):
        print("*",end=" ")    
    
    print()    
print("---------------------")









'''
A
B B
C C C
D D D D
'''    

for i in range(65,71):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()    


print("---------------------")








'''
a
b b
c c c
d d d d
'''    

for i in range(97,102):
    for j in range(97,i+1):
        print(chr(i),end=" ")
    print()        



print("---------------------")









'''
A
B C
D E F
G H I J
'''


a=65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(a),end=" ")
        a+=1
    print()    
