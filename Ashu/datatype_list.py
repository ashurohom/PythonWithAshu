
string1 = "Ashu"
print(string1)

# string1[0] = 'a'  #immutable
 
octal_no = 0o20
print(octal_no)     #16
 
octal_no2 = 0o70
print(octal_no2)    #16

print("\n****************************\n")


# # List

list1 = ["Ashu","Rohom",111,7.5,70]
print(list1,type(list1))

print(list1[0]) 
print(list1[-1]) 
print(list1[-2]) 
print(list1[:2])
print(list1[2:])
print(list1[1:4])

list1[2] = 116
print(list1)


print("\n****************************\n")

list3 = ["one","two","three","five","six","seven","eight"]
# print(list3,type(list3))

list3.insert(3,'four')
list3.append("nine")
list3.insert(0,"zero")
# list3.insert(3,"four")
print("Length : ",len(list3))
print(list3)

list3.remove("seven")
print(list3)


print("\n****************************\n")

list4 = ["one","two","three","five"]
print(list4)

list3.extend(list4)
print(list3)

list4.clear()
print(list4)

del list4
# print(list4)

print("\n****************************\n")

list5 = [10,50,30,80,20,60,30]
list5.sort()                #Asc
list5.sort(reverse=True)    #desc
print(list5)

# list4.reverse()
# print(list4)

print("\n****************************\n")


list6 = [[1,2,3],[4,5,6],[7,8,9]]
print(list6,type(list6))

element = list6[1][2]
print(element)  #6

first_col = [row[0] for row in list6]
print(first_col)    #1,4,7


print("\n****************************\n")


my_list = [5, 8, 'Tom', 7.50, 'Emma']

# slice first four items
print(my_list[:4])
# Output [5, 8, 'Tom', 7.5]

# print every second element
# with a skip count 2
print(my_list[::2])
# Output [5, 'Tom', 'Emma']

# reversing the list
print(my_list[::-1])
# Output ['Emma', 7.5, 'Tom', 8, 5]

# Without end_value
# Stating from 3nd item to last item
print(my_list[3:])


print("\n****************************\n")



# Iterating a List

mylist2 = ["Ashu","Rohom",111,7.5,"Python","Pune"]

for i in mylist2:
    print(i)

mylist2.extend([1,2,3])    
print(mylist2)