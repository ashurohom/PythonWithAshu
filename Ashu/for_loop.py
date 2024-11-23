for i in range(1,11):
    print(i,end=" ")

print("\n")

for j in range(2,21,2):
    print(j,end=" ")

print("\n")


# Example: Print sum of all even numbers from 2 to 20

sum = 0 
for s in range(2,22,2):
    sum = sum + s
print(sum)    


print("\n")
# Example: Calculate the square of each number of list

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)

sq = 0
for i in my_list:
    sq = i * i
    # print(sq,end=" ")
    print("Square Of ",i," Is ",sq)



# # Find Key In List

# name = ["ashu","tejas","sanket","krishna","nischay"]

# for a in name:
#     if name == "ashu":
#         print("Key Found")
#     else:
#         print("Key Not Found")    
    


# calculate the average of list number


list5 = [10,20,30,40,50]

sum = 0
for num in list5:
    sum = sum + num

list_size = len(list5)
avg = sum / list_size
print(avg)    


# if-else in for loop

# Example: Print all even and odd numbers


for number in range(1,11):
    if number % 2 == 0:
        print(number,"Even Number")
    else:
        print(number,"Odd Number")

print("\n")

# now using list

print("Check Odd Even Number in List")
mylists = [2,4,76,10,7,8,45,96,45,23,77,55]

for numbers in mylists:
    if numbers % 2 == 0:
        print(numbers,"Even Number")
    else:
        print(numbers,"Odd number")    

print("\n")

# break for loop

# Example: break the loop if number  is greater than 15

print("break the loop if number  is greater than 15")
list4 = [2,4,6,8,10,11,12,30,45,50]

for aa in list4:
    if aa >= 30:
        break
    else:
        print(aa)



# Continue Statement in for loop

# Count the total number of ‘a’ in a given string.

name = "bubble"
count = 0

for iii in name:
    if iii != "b":
        continue
    else:
        count = count + 1
print("'b' Count Is : ",count)




# Pass Statement in for loop
#pass is a null statement

for b in range(5):
    pass    #nothing print


