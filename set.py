# # s = set()
# # print(type(s))

# # myset = {1,2,3,4,5,2,3}
# # print(myset) #Dublicate are removed.


# # WAP to remove dublicate from list

# list = [1,2,3,4,5,2,3,4]
# count = []
# for i in list:
#     if i not in count:
#         count.append(i)
# print(count)    


# t1=(2,3,"Ashu",4,5,2)
# print(t1)
# print(t1)
# print(t1)

# set = {1,2,3,4,5}
# print(len(set))

# set.add(6)
# set.remove(6)


# # update

# # set.update(10,20) #error
# set.update([10,20,30])
# print(set)

# # copy

# s = {1,2,3,4,5}
# s1=s.copy()

# # pop
# s2=s.pop()
# print(s)

# # discard
# s.discard(100)
# print(s)

# # remove

# s2 = s.clear()
# print(s2)

# # union

# x={1,2,3}
# y={3,4,5}

# # print(x.union(y))
# print(x|y)

# print(x.intersection(y))

# # print(x.difference(y))
# print(x-y)

# print(x.symmetric_difference(y))
# print(x^y)


# # set comprehension
# s3 = {x*x for x in range(5)}
# print(s3)

#wap to using set comprehension find even number in given list.

set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {x%2 == 0 for x in set1}
set2 = {i for i in set1 if i%2==0}
print(set2)



# typecast

a1 = [1,2,3]
print(a1,type(a1))

a2 = tuple(a1)
print(a2,type(a2))

a3 = set(a1)
print(a3,type(a3))
