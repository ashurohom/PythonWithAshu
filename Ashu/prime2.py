# To check no is prime or not

num = int(input("Enter number To Check No Is Prime Or Not : "))
count = 0

for i in range(2,num):
    if num % i == 0:
        count += 1
if count == 0:
    print("Prime Number")
else:
    print("Not Prime Number")    
    