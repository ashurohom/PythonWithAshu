
a,b = 0,1
new_list = []
new_list.append(a)
new_list.append(b)

for i in range(1,11):
    c = a+b
    new_list.append(c)

    a = b
    b = c
print(new_list)





'''
thord_number = add of previous two fibonacci number.
Ex :
0=0   = 0
1=1   = 1 
2=1+0 = 1
3=1+1 = 2
4=2+1 = 3 
5=3+2 = 5
6=5+3 = 8
7=8+5 = 13
8=13+8  = 21
9=21+13 = 34
10=34+21 = 55



'''
 
