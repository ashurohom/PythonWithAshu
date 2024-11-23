a = 10

if a>15:
    print(a," is Grater than 15")
else:
    print(a, "is less than 15")    

print("\n")

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

if (num1 > num2):
    print(num1,"Grater Than",num2)
else:
        print(num2,"Grater Than",num1)    


'''Question 1: Age Check
Write a program that asks the user for their age and prints whether 
they are a child (0-12), a teenager (13-19), an adult (20-64), or a senior (65 and older).'''


age = int(input("Enter Your Age : "))

if age <= 12:
    print("You Are A Child")

elif age>=13 and age<=19:
    print("You Are A Teenager")

elif age>=20 and age<=64:
    print("You Are A Adult")

else:
    print("You Are A Older")              

    

# nested if-else

numbers1 = int(input("Enter Number 1 : "))  
numbers2 = int(input("Enter Number 2 : "))  

if numbers1 >= numbers2:
    if numbers1 == numbers2:
        print(numbers1," is equal to ",numbers2)
    else:
        print(numbers1," is grater than ",numbers2)    
else:
    print(numbers2, "grater than ",numbers1)



# Single statement suites    

digit = 100

if digit > 0 :print("Positive Number")
else:print("Negative Number")

