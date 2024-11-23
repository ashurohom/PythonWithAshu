#list=[1,2,3,4,5]
# hetrogenoius = multipal type dublicates

list = [1,2,3,4,5,5.5,'ashu',['a','b','c']]
print(list)
print(type(list))   #list

print(list[2])      #3
print(list[7][0])   #a


# accessing using indexing

print(list[6][1])   #s
print(list[6][3])   #u
print(list[0:3])    #[1,2,3]


list1 = [10,20,30,40,50,60]
print(list1[0:5])   #[10, 20, 30, 40, 50]
print(list1[0:5:2])   #[10, 30, 50]
print(list1[1:6:2])   #[20, 40, 60]
print(list1[-1:-6])   #[60, 50, 40, 30, 20, 10]





s="hello good morning"
print(s[5:11])  #good



# accessing list element using for loop

list2 = [10,20,30,40,50,60]
for i in list2:
        print(i,end=' ')
# O/P = 10 20 30 40 50 60

print()

n=len(list2)
for j in range(n):
        print(list2[j],end=' ')
# O/P = 10 20 30 40 50 60



print()
m=len(list2)
i=0
while i<m:
        print(list1[i],end=' ')
        i=i+1
# O/P = 10 20 30 40 50 60


print()
z=len(list2)
x=0
while z>0:
    print(list2[x],end=' ')
    x+=1
    z-=1



# wap to according to output "nohtyP si a gnimmargorp egaugnal" if input is "Python is a programming language"

print()
l = "Python is a programming language"
k = l.split(" ")
n=""
for i in k :
       s = i[::-1]+" "
       n+=s
print(n)       

# o/p = "nohtyP si a gnimmargorp egaugnal"





# --------------------------------------------------------------------------------------------------------------
# tip : there is no find in list

# Build Function in list
# 1)count

new_list = [1,2,4,6,1,10,2,1]
print(new_list)
print(new_list.count(1))    #3
print(new_list.count(4))    #1



# 2)index
# append = used to add element at the end of the list

new_list.append(12)
new_list.append(15)
print(new_list)


# 3)insert
# insert = used to add element in specific position

new_list.insert(2,3)
new_list.insert(6,5)
print(new_list)


# 4)extend
# extend = add list into another list

new_list2 = ['a','b','c','d']
new_list.extend(new_list2)
print(new_list)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l1.extend(l2)
print(l1)


# 5)pop
# pop = used to return and remove last element from the list.

print(l1.pop())
print(l1)

print(l1.pop())
print(l1)


# 6)remove
# remove() = remove a specific element from the list

l1.remove(4)
print(l1)


# ordering elements of list

# 7)reverse
# reverse() : used to reversed order of element present in the list

l3 = [1,2,3,4,5]
l3.reverse()
print(l3)



#8) sort
# sort : used to sort the list element in ase and desc order

l4 = [4,2,1,5,3]
l4.sort()
print(l4) 

# if we want to sort the element in desc order then use reverse=true in sort
l4.sort(reverse=True)
print(l4)


# --------------------------------------------------------------------------------------------------------------


# Aliasing and clonning list objects

# alis=asing : the process of giving another references variable to the existing list is called alliasing


x = [10,20,30,40,50]
y = x
print(x)
print(y)
print(id(x))
print(id(y))

if id(x) == id(y):
    print("Same Id")
else:
    print("Different Id")

print("-----------------")

print(id(x))
print(id(y))
y.insert(3,100)
print(x)
print(y)

m=x.copy()
m.insert(3,100)
print(y)
print(x)
print(m)





# # Counting Occurrences in a List

print("---------------------------")
lists = [12,2,3,5,6,8,1,2,3,5,2]
c = 0
x = int(input("Enter Number : "))
for i in lists:
    if i==x:
        c+=1
print('count of',x,' : ',c)        



print("===========================================")

# list Comprehensions
l=[1,2,3,4,5]
sqr = [i**2 for i in l]
print(sqr)

