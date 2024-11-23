# wap to remove duplicate from tuple

T=(1,2,3,4,5,6,2,3,1,4,5,7,8)
tup = []
for i in T:
    if i not in tup:
        tup.append(i)
print(tuple(tup))

