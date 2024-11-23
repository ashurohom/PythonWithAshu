# # Reverse for loop

# list = [10,20,30,40,50]

# for i in reversed(list):
#     print(i,end=" ")

# print("\n")
# # Reverse for loop using range()

# my_list = 5

# for a in (range(my_list,-1,-1)):
#     print(a,end=" ")


# print("\n")
# # Reverse a list using a loop

# list2 = [1,2,3,4,5]
# for b in list2[::-1]:
#     print(b,end=" ")

# print("\n")
# # Nested for loop

# # Nested for loop to print the following pattern

# num = 5
# for i in range(1,num + 1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print(" ")        


# # Nested for loop to print the following pattern

# numbers = 5
# for c in range(1,numbers + 1):
#     for d in range(1,c + 1):
#         print(c,end=" ")
#     print(" ")    


        # print("---------------------------")
    # While loop inside for loop

for e in range(1,6):
    print("Multiplication : ",e)

    count = 1

    while count < 11:
        print(e * count,end=" ")
        count = count + 1
    print("\n")




#Accessing the index in for loop
# range , enumerate()

my_list = [1,3,4,7,12,15]
size = len(my_list)

for f in range(size):
    print("[",f,"]","=",my_list[f])  



# Split function in String
print("\n")
name = '''My name is Ashitosh, i am B.Tech Student'''

for names in name.split():
    print(names)



#List Comprehension

lista = ['ashu','sanket','teja','nischy','kajal','sakshi','om']

list_comp = [x for x in lista if "a" in x]
print(list_comp)

