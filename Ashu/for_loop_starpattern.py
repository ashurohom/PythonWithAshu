a = 5

for a in range(1,6):
    for b in range(1,6):
        print("*",end=" ")
    print("\n")


print("--------------------------")    


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")        


print("--------------------------")    
    

for i in range(1,10,2):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")        


print("--------------------------")


for c in range(6):
    for d in range(c,6):
        print("*",end=" ")
    print("\n")    

print("--------------------------")


for c in range(6):
    for d in range(c,6):
        print(c,end=" ")
    print("\n")    

print("--------------------------")


for e in range(5):
    for f in range(1,e-1):
        print("*",end=" ")
    print("\n")    