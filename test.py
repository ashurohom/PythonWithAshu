# find given number is prime or not

# num = int(input("Enter Number : "))    

# if num > 1:
#     for i in range(2,num):
#         if num % i == 0:
#             print(f'{num} is not prime number')
#             break
#     else:
#         print(f'{num} is Prime number')        
# else:
#     print(f'{num} is not prime number')


# Print prime number between 1 to 150

for i in range(2,150):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")    