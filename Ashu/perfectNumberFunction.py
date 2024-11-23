num = int(input("Enter Number To Check Number is Perfect No or Not : "))

def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum+=i
    return sum == num

if perfect_num(num):
    print(f'{num} is perfect number')        
else:
        print(f'{num} is not perfect number')            