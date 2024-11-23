# prime number
# no is only divided by itself.

num = int(input("Enter number To Check No Prime or Not :  "))
value = 0

for i in range(1,num+1):
    if num % i == 0:
        value += 1
if value > 2:
    print("Not Prime Number")
else:
    print("Prime Number")            



#sort the prime number in given list.

# a = [2,5,6,13,14,31,45,61,71,75,97,98]
# c = 0
# prime_list = []

# for j in a:
#     if a % j == 0:
#         c += 1
#         if c < 2:
#             prime_list.append(c)
