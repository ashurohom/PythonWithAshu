# Exception Handeling

# An exception is an event that occurs during the execution of 
# programs that disrupt the normal flow of execution

'''
Syntax : 

try:
    statement in try bllock

except:
    executed when exception occured in try block

finally:
    always execute

'''

# Example 1
try:
    a=int(input("Enter RollNo : "))
    print("Rollno : ",a)
except:
    print("Invalid Input")

print("excute Outside Body of try except")


# Example 2

try:
    num = int(input("Enter Integer Number : "))
    print(f"The Number {num} is integer")
except:
    print("Invalid Input Number")
finally:
    print("In the finally")    


