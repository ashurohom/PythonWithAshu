'''
3. Check If a Number is Prime
Write a function named is_prime(num) that takes an integer as input and returns True if it is a prime number, otherwise False.
Example:
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False
'''

def is_prime(num):
    count=0
    for i in range(1,num):
        if num%2==0:
            count+=1
    if count > 2:
        return False
    else:
        return True
    
print(is_prime(7))    