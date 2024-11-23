'''
2 
4 4
6 6 6
8 8 8 8
10 10 10 10 10

'''

a=0
for i in range(0,6):
    for j in range(i):
        print(a,end=" ")
    a+=2    
    print()    

print("------------------------------")







'''
2
4 6
8 10 12
14 16 18 20
'''    

z=2
for x in range(1,6):
    for y in range(x):
        print(z,end=" ")
        z+=2
    print()    


print("------------------------------")


 
'''
2
4 4
8 8 8
16 16 16 16
'''

count=2
for i in range(1,6):
    for j in range(i):
        print(count,end=" ")
    count*=2
    print()

print("------------------------------")
