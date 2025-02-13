# find given number is prime or not

num = int(input("Enter Number : "))    

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(f'{num} is not prime number')
            break
    else:
        print(f'{num} is Prime number')        
else:
    print(f'{num} is not prime number')