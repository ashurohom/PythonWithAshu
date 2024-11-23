# Python program to print the prime numbers from 1 to n.

num = int(input("Enter Number : "))

def prime_number(num):
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" ")    
    return i
prime_number(num)





