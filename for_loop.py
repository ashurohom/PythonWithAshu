# # wap to print even numbers between 0 to 100

# for i in range(0,101,2):
#     print(i)


# for j in range(1,101,2):
#     print(j)

# for a in range(1,101):
#     if a % 2 == 0:
#         print(a,end=" ")
#     else:
#         pass 

# print("\n")

# for a in range(1,101):
#     if a % 2 != 0:
#         print(a,end=" ")
#     else:
#         pass        


# wap to check given no is prime or not

# print("\n")
# num = int(input("Enter Number : "))

# if num % 1:
#     print("Non Prime")

# elif num % num:
#     print("Non Prime")

# else:
#     print("Prime Number")







print("*********************************")


# limit = 100  # Change this to any number you want to check up to

# for num in range(2, limit + 1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num,end=" ")


count = 0

for b in range(101):
    if b % 2 != 0:
        count += 1
    
print("Odd Count : ",count)         