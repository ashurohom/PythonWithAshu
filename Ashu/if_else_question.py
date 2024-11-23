'''Password Check
write a program that check a password, accept password from user and check the password
is corrcet or not, store the password in a variable'''


password = input("Enter Your Password : ")

if password == "Radha":
    print("Corrcet Password")

else:
    print("Wrong Password")



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



print("\n")


'''Question 2: Even or Odd
Create a program that asks the user for a number and prints whether the number is even or odd'''


number = int(input("Enter A Number : "))

if number == 0:
    print(number,"Is Zero")
elif (number%2)==0:
    print(number,"Is Even Number")
else:
    print(number,"Number Is Odd")   


print("\n")


'''Question 3: Simple Grade Calculator
Ask the user for a score (0-100) and print the corresponding grade:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 59 and below'''         


score = float(input("Enter Your Score : "))
dtype = type(score)

if score >= 90 and score <= 100:
    print("A Grade")

elif score >= 80 and score <= 89:
    print("B Grade")

elif score >= 70 and score <= 79:
    print("C Grade")

elif score >= 60 and score <= 69:
    print("D Grade")

else:
    print("F Grade")


print("\n")


'''Question 4: Positive, Negative, or Zero
Write a program that prompts the user for a number and prints whether it is positive, negative, or zero.'''


num = int(input("Enter Number : "))

if num == 0:
    print("Number Is Zero")

elif num >= 1:
    print("Number Is Positive")

else:
    print("Number Is Negative")         


print("\n")


'''Question 5: Compare Two Numbers
Ask the user to input two numbers and then print a message indicating whether 
the first number is greater than, less than, or equal to the second number.'''


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

if(num1 == num2):
    print(num1,"Equal To",num2)

elif num1 > num2:
    print(num1,"grater Than",num2)

else:
    print(num1,"Less Than",num2) 

