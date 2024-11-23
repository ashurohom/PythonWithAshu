# #wap to calculate prime number using list Comprehensions

# # find max element in given list.
# # 1)using sort method

# l=[1,2,3,4,5]
# l.sort()
# print(l[-1])

# l.sort(reverse=True)
# print(l[0])

# # IMP
# # 2)
# a = [30,20,50,40,10]
# larg = a[0]
# for val in a:
#     if val > larg:
#         larg = val
# print(larg)


# 3) print 2nd max number

l=[1,2,3,4,5]
l.sort()
print(l[-2])

l.sort(reverse=True)
print(l[1])


b = [30,20,50,40,10]
larg = b[0]
larg2 = b[0]
for val in b:
    if val > larg:
        larg2=larg
        larg = val
    elif val>larg2 and  val != larg:
            larg2=val
print(larg2)





# 4) print 3rd max number

l=[1,2,3,4,5]
l.sort()
print(l[-3])

l.sort(reverse=True)
print(l[2])

b = [30,20,50,40,10]
larg = b[0]
larg2 = b[0]
larg3 = b[0]
for val in b:
    if val > larg:
        larg3=larg2
        larg2=larg
        larg = val
    elif val>larg2 and  val != larg:
            larg2=val
             
    elif val>larg2 and  val != larg2:
            larg3=val
             
print(larg3)



