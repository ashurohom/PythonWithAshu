# For time complixity

num = int(input("Enter Number : "))
count = 0

for i in range(2,num//2+1):
    if num % i == 0:
        count += 1

if count == 0:
    print("Prime Number")
else:
    print("Not Prime Number")

