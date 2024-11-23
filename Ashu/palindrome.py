# wap to check if a list contains a pallindrome of elements.

list11 = [1,2,3,2,1]
list1 = ['r','a','d','a','r','p']

copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print("Pallindrome")
else:
    print("Not Pallindrome")    